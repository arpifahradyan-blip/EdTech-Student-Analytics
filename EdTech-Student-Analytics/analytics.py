# analytics_visualizer.py
import matplotlib.pyplot as plt
import numpy as np

def generate_soft_skills_chart():
    fig, ax = plt.subplots(figsize=(10, 5))

    soft_skills = [
        'Acceptance of Errors\n(Growth Mindset)',
        'Focus & Concentration\n(Attention)',
        'Persistence & Grit\n(Resilience)',
        'Intrinsic Work Ethic\n(Self-Motivation)'
    ]

    baseline_scores = [20, 30, 25, 20]
    result_scores = [85, 75, 70, 50]  # 50% Intrinsic work ethic

    y = np.arange(len(soft_skills))
    height = 0.35

    rects1 = ax.barh(y + height/2, baseline_scores, height, label='Baseline (Before)', color='#e11d48', alpha=0.85)
    rects2 = ax.barh(y - height/2, result_scores, height, label='Current Result (2 Months)', color='#059669', alpha=0.85)

    ax.set_xlabel('Development Level (%)', fontsize=11, fontweight='bold')
    ax.set_title('Student Soft Skills Progress (Impact of Tutor Intervention)', fontsize=13, fontweight='bold', pad=15)
    ax.set_yticks(y)
    ax.set_yticklabels(soft_skills, fontsize=10, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.set_xlim(0, 105)

    for rect in rects1:
        width = rect.get_width()
        ax.annotate(f'{width}%', xy=(width, rect.get_y() + rect.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points", ha='left', va='center', fontsize=9, fontweight='bold', color='#be123c')

    for rect in rects2:
        width = rect.get_width()
        ax.annotate(f'{width}%', xy=(width, rect.get_y() + rect.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points", ha='left', va='center', fontsize=9, fontweight='bold', color='#047857')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig('simple_soft_skills_updated.png', dpi=300)
    print("Chart saved as 'simple_soft_skills_updated.png'")

if __name__ == "__main__":
    generate_soft_skills_chart()