import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({
    'axes.titlesize': 18,
    'axes.labelsize': 14,
    'xtick.labelsize': 13,
    'ytick.labelsize': 13,
    'legend.fontsize': 12,
    'legend.title_fontsize': 14,
})

# def decompose_data(df, data_retain, data_decompose):
#     df_decompose = pd.DataFrame(columns=['type', 'value'] + columns_retain)
#
#     for index, row in df.iterrows():
#         for column in columns_decompose:
#             df_entry = row[columns_retain]
#             df_entry['type'] = column
#             df_entry['value'] = row[column]
#
#             df_decompose = df_decompose.append(df_entry, ignore_index=True)
#     return df_decompose


# ===Plot comparing PPO and TD3
df_ppo = pd.read_csv('data/correlation/ppo_decomposed_allPatients.csv')
# df_ppo = pd.read_csv('ppo_decomposed.csv')
df_ppo['algorithm'] = 'PPO'

df_td3 = pd.read_csv('data/correlation/td3_decomposed_allPatients_rev1.csv')
# df_td3 = pd.read_csv('td3_decomposed.csv')
df_td3['algorithm'] = 'TD3'

df_dpg = pd.read_csv('data/correlation/dpg_decomposed_allPatients.csv')
df_dpg['algorithm'] = 'DPG'

df_ddpg = pd.read_csv('data/correlation/ddpg_decomposed_allPatients.csv')
df_ddpg['algorithm'] = 'DDPG'

#
df = pd.concat([df_ppo, df_td3, df_dpg, df_ddpg], ignore_index=True)
print(df.columns)
df = df[df['type'] != 'cgm_mean']  # Remove the cgm_mean value

new_labels = ["t-" + str(i) for i in range(12, 0, -1)]
insulin_labels = ["i" + str(i) for i in range(1, 13)]
glucose_labels = ["x" + str(i) for i in range(1, 13)]

df_insulin = df[df['type'].isin(insulin_labels)]
df_glucose = df[df['type'].isin(glucose_labels)]

# Plot glucose
for patient in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sns.boxplot(
        data=df_glucose[df_glucose['subject'] == patient], x="type", y="value", hue='algorithm',
        fill=False, palette="deep", showfliers=False)
    plt.title(f'Patient {patient}')
    plt.xlabel('Glucose')
    plt.ylabel('Correlation')
    plt.ylim(-0.5, 1.05)
    plt.xticks(ticks=plt.gca().get_xticks(), labels=new_labels)  # Change x-axis labels
    plt.gca().invert_xaxis()  # Reverse the x-axis

    plt.show()

for algo in ['PPO', 'TD3', 'DDPG', 'DPG']:
    sns.boxplot(
        data=df_glucose[df_glucose['algorithm'] == algo], x="type", y="value", hue='subject',
        fill=False, palette="deep", showfliers=False)
    plt.title(f'{algo}')
    plt.xlabel('Glucose')
    plt.ylabel('Correlation')
    plt.ylim(-0.5, 1.05)
    plt.xticks(ticks=plt.gca().get_xticks(), labels=new_labels)  # Change x-axis labels
    plt.gca().invert_xaxis()  # Reverse the x-axis
    plt.legend(ncol=2, title=  "Patient")


    plt.show()

# Plot Insulin
for patient in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sns.boxplot(
        data=df_insulin[df_insulin['subject'] == patient], x="type", y="value", hue='algorithm',
        fill=False, palette="deep", showfliers=False)
    plt.title(f'Patient {patient}')
    plt.xlabel('Insulin')
    plt.ylabel('Correlation')
    plt.ylim(-0.5, 1.05)
    plt.xticks(ticks=plt.gca().get_xticks(), labels=new_labels)  # Change x-axis labels
    plt.gca().invert_xaxis()  # Reverse the x-axis

    plt.show()

for algo in ['PPO', 'TD3', 'DDPG', 'DPG']:
    sns.boxplot(
        data=df_insulin[df_insulin['algorithm'] == algo], x="type", y="value", hue='subject',
        fill=False, palette="deep", showfliers=False)
    plt.title(f'{algo}')
    plt.xlabel('Insulin')
    plt.ylabel('Correlation')
    plt.ylim(-0.5, 1.05)
    plt.xticks(ticks=plt.gca().get_xticks(), labels=new_labels)  # Change x-axis labels
    plt.gca().invert_xaxis()  # Reverse the x-axis
    plt.legend(ncol=2, title=  "Patient")

    plt.show()