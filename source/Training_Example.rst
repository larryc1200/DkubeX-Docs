
.. include:: Role_Header.txt

.. _training-example:

Training Example
#################

* Explain reason for the example - to take the user through a real training exercise withing DKubeX
* Overview of the example flow
* This section should be very detailed, with block diagrams and screenshots to help describe the process & ensure that the user is following along

Training Flow
**************

* Details of the steps involved in training
* Description of tools and processes
* I am not sure how the local vs remote training differ, so you can decide how best to partition them
* I have included 2 sections, but it's likely that there is a lot of overlap - based on that, you may find that a single section witih tabs for where they diverge makes more sense

Local Training
===================


Remote Training
=================

* One difference between local training and remote will be whether an IDE is used.  The assumption is that for remote training, that would have been done on the other cluster, so the training will be primarily a batch run.

Accessing the Code
********************

* Repo for the code
* Details of finding the right files

Analyzing the Code
********************

* I am assuming that you'll be showing the code in Jupyter (at least for local training)
* Show how to get the code into JupyterLab

Description of Program
***********************

* Explanation of the code & data
* A detailed explanation of instrumenting the code for Ray execution & MLFlow are important

Training Details
*****************

* Step by step recipe of the batch training, with any required commands
* The local and remote training should be as self-contained as possible.  That is, there should be a minimum of jumping around and referencing.  It may be easier to have 2 complete sections, or one section with tabs where they differ.  Or the first part may differ but then the follow-on may be the same.

Viewing the Progress
*********************

* Since this is a Ray execution, the progress will be based on the output to the terminal, through the DkubeX UI, and through the Ray dashboard.
* I am unsure exactly how this will look, so you can decide on the subsections once the flow is well-understood
* The log files will be important to output - both from Ray and DKubeX
* I expect that you'll be showing the DKubeX tabs that deal with MLflow, Metrics, Cluster, & Logs as required.  The focus will be on showing how they work with the example, with links to the more detailed sections later in the guide.

Viewing the Metrics
********************

* Looking at the training metrics
* Comparing them - there may a need to do 2 runs for that
* Highlighting what to look for