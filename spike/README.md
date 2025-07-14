# Spike Data Analysis

This folder contains scripts to do analysis on spike-sorted data output from Phy. It contains scripts to do single cell analyses (Wilcoxon tests, raster plots, and bootstrap firing rate comparisons), PCA analyses and trajectory visualizations, classifiers to predict  behavioral events based on population activity, and functions to normalize firing rates. 


```
+--------------------------------------------------------------------------+                       
|  SpikeCollection                                                         |                       
+--------------------------------------------------------------------------+
| - path                                                                   |    
| - event_dict                                                             | 
| - subject_dict                                                           |
| - sampling_rate                                                          |
| - recordings[]                                                           |
+--------------------------------------------------------------------------+
| + __init__()                                                             |
| + make_collection()                                                      |
| + analyze()                                                              |
| + recording_details()                                                    | 
+--------------------------------------------------------------------------+
|                        |                                                 |
|                        | contains many                                   |
|                        v                                                 |
|            +----------------------------+                                |
|            |  SpikeRecording            |                                |
|            +----------------------------+                                |
|            | - path                     |                                |
|            | - name                     |                                |                +--------------------------+
|            | - sampling_rate            | ----------------------------------------------> | firing_rate_calculations |
|            | - subject                  |  calculates                    |                +--------------------------+
|            | - event_dict               |  attributes for                |                | + get_spiketrain()       |
|            | - timestamps               |<------------------------------------------------| + get_firing_rate()      |
|            | - unit_array               |                                |                +--------------------------+
|            | - labels_dict              |                                |
|            | - unit_timestamps          |                                |
|            | - spiketrain               |                                |
|            | - unit_spiketrains         |                                |
|            | - timebin                  |                                |
|            | - ignore_freq              |                                |
|            | - smoothing_window         |                                |
|            | - mode                     |                                |
|            | - freq_dict                |                                | 
|            | - good_neurons             |                                |
|            | - analyzed_neurons         |                                |
|            | - unit_firing_rates        |                                |
|            | - unit_firing_rate_array   |                                |
|            +----------------------------+                                |
|            | + __init__()               |                                |
|            | + set_subject()            |                                |
|            | + set_event_dict()         |                                |   
|            | + event_snippets()         |                                |
|            | + unit_event_firing_rates()|                                |
|            | + event_firing_rates()     |                                |
|            +----------------------------+                                | ----------------------------------------+
+--------------------------------------------------------------------------+                                         |
      |                                  |                               |                                           |
      | used as input for                | used as input for             | used as input for                         |
      v                                  v                               v                                           v
+--------------------------+      +----------------------------+     +---------------------------------+       +--------------+
| normalization            |      | pca_trajectories           |     | single_cell                     |       | decoders     |  
+--------------------------+      +----------------------------+     +---------------------------------+
| + zscore_global()        |      | + geodesic_distances()     |     | + wilcoxon_collection()         |
| + zscore_baseline_event()|      | + distance_bw_trajectory() |     | + wilcoxon_event1v2_collection()|
| + zscore_pre_event()     |      | + pca_matrix()             |     | + fisher_exact_wilcoxon()       |
| + zscore_plot()          |      | + avg_trajectories_pca()   |     | + bootstrap()                   |
+--------------------------+      | + trial_trajcetories_pca() |     | + plot_raster()                 |
                                  | + condition_pca()          |     +---------------------------------+
                                  | + LOO_PCA()                |
                                  +----------------------------+
                                  |returns a PCAResult object  |
                                  +----------------------------+
                                  | - raw_data                 |
                                  | - matrix_df                |
```