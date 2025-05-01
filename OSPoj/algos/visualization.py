# visualization.py
import matplotlib.pyplot as plt

from matplotlib import patheffects  
import io

def generate_chart(results):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    algorithms = list(results.keys())
    faults = list(results.values())
    
    if len(algorithms) != 3:
        raise ValueError("Need results for FIFO, LRU, and OPT")
    
    bars = ax.bar(algorithms, faults, 
             color=['#818cf8', '#fbbf24', '#7f00ff'],
             width=0.7,
             edgecolor='white')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.3,
                f'⚡{height}',
                ha='center', va='bottom',
                fontsize=14,
                color='white')
    
    ax.set_xticklabels([
        f'{algorithms[0]}\n(FIFO)',
        f'{algorithms[1]}\n(LRU)',
        f'{algorithms[2]}\n(OPT)'
    ])
  
    ax.yaxis.grid(True, linestyle='--', alpha=0.4)
    ax.spines['bottom'].set_color('#475569')
    ax.spines['left'].set_color('#475569')
    
    best = min(results.values())
    ax.annotate(f"★ Best performance: {best} faults",
                xy=(0.5, 0.87),  
                xycoords='axes fraction',
                ha='center', 
                va='top',
                bbox=dict(boxstyle="round,pad=0.3",
                          fc="#1e293b", ec="#475569",
                          lw=1.5),
                fontsize=12, 
                color='white')
    plt.subplots_adjust(top=0.75)
    
    img = io.BytesIO()
    plt.savefig(img, format='png', dpi=120, 
               bbox_inches='tight', facecolor='#0f172a')
    plt.close()
    
    return img