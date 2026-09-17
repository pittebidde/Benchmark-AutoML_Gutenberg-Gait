<h1> Benchmark-AutoML_Gutenberg-Gait </h1>
This is a quick roundup of what you need to know to run the benchmark itself. From my own xerpience, this will take roughly 4-5 hours to setup and 30 hours to run (50% Fitting, 50% SHAP).
All scripts have been numbered according to their chronological usage. It is important to note, that the helper scripts "persistent_predict_server_..." are not enumerated and are not activly run, instead only run as a serverise function using Docker.

To provide a foundation for the corresponding paper, the results for the paper are archived under the folder "results".
The folder provides all benchmarks and importance_long, the final results from which the findings of the paper can be reconstructed.
The results from the benchmark itself can be run through "03_benchmark-visualization", while the archived Shap results have a helper script in its results folder "shap_helper".

<h2> Benchmarking </h2>
If possible, the code was seeded so to make reproducability more reliable. This does not mean, that it is fully reproducible and therefore results may very!

<h3> Running the Dockerfiles </h3>
I personally used three seperate folders (Dockerfile_AutoGluon, Dockerfile_pytorch, Dockerfile_sklearn, Dockerfile_SHAP) for troubleshooting and ease of use.
To make it a bit more structured, i decided to rename the Dockerfiles to its corresponding name and put it in one overarching folder "Dockerfiles".

<h3> Running the benchmark </h3>
In order to not risk ownership of data, the Gutenberg Gait Database is not included in this scriptpackage. One needs to download all seperate .csv files and install them accordingly. (e.g /GutenbergGaitDatabase/..)
One can only run selected tasks, yet the JSON file will be build corrispondingly. 
!!!! The benchmark overrides the safed models, so if one wants to run a shap comparison along multiple time budgets, run the benchmark sequencially and safe the results seperatly !!!!

<h2> SHAP bridges </h2>
The benchmark is build as a Windows-Linux function, meaning that the SHAP environment NEEDS TO be run in a windows container (e.g. visuals tudio code kernel), while the serverside needs to be initialized using the linux based docker systems. Before starting, the persistent_predict scripts need to be safed in the corresponding workfolder under the corresponding container.



