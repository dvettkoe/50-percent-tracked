# 50-percent-tracked
Custom python script used to process .TXT files derived from wrMTrck Plugin in ImageJ for analysis of swimming behaviour in C. elegans.

1. Analyze your videos of swimming C. elegans using the ImageJ Plugins wrMTrck (https://www.phage.dk/plugins/wrmtrck.html)
2. Validate tracking (remove non-worm objects, non-swimming events, ...)
3. Create a directory containing your TXT files for each respective experiment in subfolders 
   (eg. C:\Exp-Day_XXYYZZ\exp1
                         \exp2
                         \...)
4. Start Python script "only_50%_time_tracked.py" and choose recently created directory folder.
5. Finished: You will fnd your data for plotting as XLSX files in respective "tracks_processed" folders in the subdirectories of each experiment.
