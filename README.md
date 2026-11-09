# Data Quality Rules and Pipeline Observability

An automated data validation starter that evaluates uniqueness, completeness, numeric ranges, and dataset freshness against simple policy rules. Produces a machine-readable quality report with pass/fail counts and actionable failure details. Designed to represent pre-production quality gates and observability checks for batch data pipelines.

## Quick start

```bash
python quality.py --input samples/transactions.csv --output output/report.json
python -m unittest discover -s tests -v
```

## Architecture and scope

Runs without external services and exits nonzero when a dataset fails quality gates. Checks can be adapted to Great Expectations, dbt tests or cloud monitoring alerts.

**Portfolio note:** Original educational starter code, not a production deployment. Use only synthetic/public datasets, document your own extensions, and test integrations before claiming production experience.
