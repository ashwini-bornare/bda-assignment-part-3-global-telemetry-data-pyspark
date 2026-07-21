# Part 3 - PySpark Implementation & Resilience

This document explains how to run and evaluate **Part 3** of the assignment:

- Transformations and Actions
- Narrow vs Wide dependencies
- Skew mitigation using salting and partitioning
- Fault tolerance using RDD lineage
- Checkpointing for long lineage

## Part 3 Notebook Path

The Part 3 notebook is located at:

`notebooks/Untitled.ipynb`

## Project Paths Used in Part 3

- Telemetry generator script:
  `synthetic-data-generator.py`
- Generated telemetry dataset folder:
  `data/`
- Notebook folder mounted into Jupyter:
  `notebooks/`

## Prerequisites

- Docker Desktop running
- `docker-compose.yaml` present in project root
- Telemetry JSON dataset available in `data/` (for example `telemetry_records_10000.json`)

## 1) Generate Input Data (if needed)

From project root:

```bash
python synthetic-data-generator.py
```

This creates a JSON file in:

`data/telemetry_records_<N>.json`

## 2) Start Jupyter + PySpark

From project root:

```bash
docker compose up -d
```

Then open Jupyter in browser:

`http://localhost:8888`

## 3) Open Part 3 Notebook

Open:

`/home/jovyan/work/Untitled.ipynb`

Note:
- Host path: `notebooks/Untitled.ipynb`
- Container path (mounted): `/home/jovyan/work/Untitled.ipynb`

## 4) Run the Notebook

Run cells top to bottom. The notebook demonstrates:

1. Ingestion of historical telemetry JSON
2. Average engine temperature per vehicle model
3. Narrow transformations (`filter`, `select`)
4. Wide transformations (`repartition`, `groupBy` + `agg`)
5. Hash partitioning strategy
6. Salting strategy for skewed vehicle keys
7. RDD lineage inspection (`toDebugString`)
8. Checkpointing after long iterative lineage
9. Writing output averages to disk

## 5) Expected Outputs

- Console output showing schema, counts, and aggregation results
- Execution plan (`explain`) indicating shuffle stages
- Lineage output before/after checkpoint materialization
- Output CSV folder (example):
  `output_average_temperature/`

## Troubleshooting

- If input file is not found:
  ensure the JSON exists under `data/` on host, mapped to `/home/jovyan/data/` in container.
- If notebook kernel cannot run Spark:
  restart container and notebook kernel.
- If path mismatches occur:
  use container-visible paths inside notebook (for data: `/home/jovyan/data/...`).

## Quick Verification Checklist

- Data read succeeds from JSON
- Average temperature per `vehicle_model` is shown
- Skew mitigation cells run without error
- `toDebugString()` output is visible
- Checkpoint section executes and lineage truncation is demonstrated
