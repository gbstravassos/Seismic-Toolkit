"""Small executable CLI for the synthetic demonstration."""

from __future__ import annotations

import argparse
import json

from .pipeline import run_synthetic_demo


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a synthetic seismic time-shift example")
    parser.add_argument("--dt", type=float, default=0.001, help="Sampling interval in seconds")
    parser.add_argument("--delay-samples", type=int, default=4, help="Monitor delay in samples")
    args = parser.parse_args()
    result = run_synthetic_demo(dt=args.dt, delay_samples=args.delay_samples)
    clean = {key: value for key, value in result.items() if key not in {"baseline", "monitor"}}
    print(json.dumps(clean, indent=2))


if __name__ == "__main__":
    main()
