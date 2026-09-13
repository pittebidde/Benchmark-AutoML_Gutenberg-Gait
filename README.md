<h1> Benchmark-AutoML_Gutenberg-Gait </h1>
This is a quick roundup of what you need to know to runt he benchmark itself. Frommy owne xerpience, this will take roughly 4 hours to setup and 20 hours to run.
All scripts have been numbered according to their chronological usage. It is important to note, that the helper scripts "persistent_predict_server_..." are not enumerated and are not activly run, instead only initialised.

<h2> Using Docker to run the Benchmark </h2>

<h3> Running the Dockerfiles </h3>
I personally used three seperate folders (Dockerfile_AutoGluon, Dockerfile_pytorch, Dockerfile_sklearn, Dockerfile_SHAP) for troubleshooting and ease of use.
To make it a bit more structured, i dcedided to rename the Dockerfiles to its corresponding name and put it in one overarching folder "Dockerfiles".


<h2> Using Docker to run the Benchmark </h2>



<h2> Results </h2>
If possible, the code was seeded so to make reproducability more reliable. This does not mean, that it is fully reproducible and therefore Results may very!
To provide a foundation for the corresponding paper, the results are archived under the folder "results"
