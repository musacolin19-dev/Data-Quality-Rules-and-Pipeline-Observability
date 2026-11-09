import argparse,csv,json
from datetime import date,datetime
from pathlib import Path

def evaluate(rows,required=('transaction_id','amount','day'),unique='transaction_id',as_of=None,max_age_days=14):
    as_of=as_of or date.today()
    issues,seen=[],set()
    for index,row in enumerate(rows,1):
        for field in required:
            if not str(row.get(field,'')).strip():issues.append({'row':index,'rule':'not_null','field':field})
        value=row.get(unique)
        if value in seen:issues.append({'row':index,'rule':'unique','field':unique})
        seen.add(value)
        try:
            if float(row['amount']) < 0:issues.append({'row':index,'rule':'nonnegative','field':'amount'})
        except (KeyError,ValueError,TypeError):issues.append({'row':index,'rule':'numeric','field':'amount'})
        try:
            day=date.fromisoformat(row['day'])
            if (as_of-day).days > max_age_days:issues.append({'row':index,'rule':'freshness','field':'day'})
        except (KeyError,ValueError,TypeError):issues.append({'row':index,'rule':'date','field':'day'})
    return {'rows':len(rows),'passed':not issues,'issues':issues,'issue_count':len(issues)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',default='output/report.json');p.add_argument('--as-of',default='2026-01-05');a=p.parse_args()
    with Path(a.input).open(newline='') as f:report=evaluate(list(csv.DictReader(f)),as_of=date.fromisoformat(a.as_of))
    outfile=Path(a.output);outfile.parent.mkdir(parents=True,exist_ok=True);outfile.write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
    if not report['passed']:raise SystemExit(1)
if __name__=='__main__':main()
