"""Redraw manuscript Fig. 1A from the checked-in likelihood curves."""

import argparse
import os
from pathlib import Path

os.environ.setdefault('MPLCONFIGDIR', '/tmp/dmop-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=HERE / 'curves.csv')
    parser.add_argument('--output', type=Path, default=HERE.parents[1] / 'imgs/095/mop.png')
    args = parser.parse_args()
    curves = np.genfromtxt(args.data, delimiter=',', names=True)
    plt.style.use(HERE / 'figure.mplstyle')
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(curves['gamma'], curves['particle_filter'], linestyle='dashdot', label='Particle-filter estimate')
    ax.plot(curves['gamma'], curves['alpha_1'], label=r'$\alpha=1$')
    ax.plot(curves['gamma'], curves['alpha_097'], label=r'$\alpha=0.97$')
    ax.plot(curves['gamma'], curves['alpha_0'], label=r'$\alpha=0$')
    ax.set_xticks([17.6, 17.8, 18.0, 18.2, 18.4])
    ax.set_xlabel('Recovery Rate')
    ax.set_ylabel('Log-Likelihood')
    ax.axvline(18, linestyle='--', color='black', label=r'Baseline $\phi=18$')
    ax.legend()
    fig.tight_layout()
    # No caption or large panel label in the exported plot.
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, bbox_inches='tight', dpi=100)
    plt.close(fig)


if __name__ == '__main__':
    main()

