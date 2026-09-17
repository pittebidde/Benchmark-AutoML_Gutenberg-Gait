<h1> Benchmark-AutoML_Gutenberg-Gait </h1>
This is a quick roundup of what you need to know to run the benchmark itself. From my own xerpience, this will take roughly 4 hours to setup and 30 hours to run (50% Fitting, 50% SHAP).
All scripts have been numbered according to their chronological usage. It is important to note, that the helper scripts "persistent_predict_server_..." are not enumerated and are not activly run, instead only run as a serverise function using Docker.

For all porpuses of the paper, this benchmark was run in one go, but users can run 

<h2> Using Docker to run the Benchmark </h2>

<h3> Running the Dockerfiles </h3>
I personally used three seperate folders (Dockerfile_AutoGluon, Dockerfile_pytorch, Dockerfile_sklearn, Dockerfile_SHAP) for troubleshooting and ease of use.
To make it a bit more structured, i dcedided to rename the Dockerfiles to its corresponding name and put it in one overarching folder "Dockerfiles".


<h2> Using Docker to run the Benchmark </h2>


<h2> SHAP bridges </h2>
The benchmark is build as a Windows-Linux function, meaning that the SHAP environment can be run in a windows container (e.g. visuals tudio code kernel), while the serverside needs to be initialized using the linux based docker systems. Before starting, the persistent_predict scripts need to be safed in the corresponding workfolder under the corresponding container.

<h2> Results </h2>
If possible, the code was seeded so to make reproducability more reliable. This does not mean, that it is fully reproducible and therefore results may very!
To provide a foundation for the corresponding paper, the results for the paper are archived under the folder "results".
The folder provides all benchmarks and importance_long, the final results from which the results of the paper can be reconstructed.
