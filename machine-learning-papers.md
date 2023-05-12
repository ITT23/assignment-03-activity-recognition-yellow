# Questions about Machine Learning Papers

## What are some common use cases for machine learning in practical applications or research prototypes?

[1] most important reason for using a machine learning system is precisely that "the desired behavior cannot be
effectively implemented in software logic without dependency on external data".


## Which problems of machine learning do the authors of the papers identify?

[1] Technical dept (introduced by Ward Cunningham in 1992 as a way to help quantify the cost of such decisions):

        - massive ongoing maintenance costs at the system level
        - system brittleness
        - reduced rates of innovation

[1] machine learning packages have all the basic code complexity issues as normal code, but also have a larger system-level complexity that can create hidden debt.
    Thus, refactoring these libraries, adding better unit tests, and associated activity is time well spent but does not necessarily address debt at a systems level.
    subtly erode abstraction boundaries at a system-level.
    creation of unintended tight coupling of otherwise disjoint systems through re-use of input signals
    large masses of “glue code” or calibration layers that can lock in assumptions because machine learning treated as black boxes
    Changes in the external world may make models or input signals change behavior in unintended ways

    Entanglement: machine learning models are machines for creating entanglement and making the isolation of improvements effectively impossible.
                    CACE principle: Changing Anything Changes Everything.
                    result of such changes is that prediction behavior may alter, either subtly or dramatically, on various slices of the distribution.
                some strategies may help but its also means that shipping the first version of a machine learning system is easy, but that making subsequent improvements is unexpectedly difficult.

    Hidden Feedback Loops: 
                Systems that learn from world behavior are clearly intended to be part of a feedback loop
                the system will slowly change behavior because of feature adjustments and updating with new data.
                Gradual changes not visible in quick experiments make analyzing the effect of proposed changes extremely difficult, and add cost to even simple improvements.

    Undeclared Consumers:
    Making predictions from a machine learning model accessible to other systems can cause a visibility debt. Which means that without access controls, it is possible for some of these consumers to be undeclared consumers, consuming the output of a given prediction model as an input to another component of the system. 

    Unstable Data Dependencies:
    consuming signals as input features that are produced by other systems has the potential risk that some input signals are unstable, meaning that they qualitatively change behavior over time. As a result, changes and improvements to the input signal may be regularly rolled out, without regard for how the machine learning system may be affected. 
    This causes input signals to may have arbitrary, sometimes deleterious, effects that are costly to diagnose and address.


    Underutilized Data Dependencies:
    That is understood to mean packages that are mostly unneeded and are costly, since they make the system unnecessarily vulnerable to changes. 
    Underutilized dependencies can creep into a machine learning model in several ways like for example legacy features or bundled features.

    Static Analysis of Data Dependencies:
    One of the key issues in data dependency debt is the difficulty of performing static analysis, because it requires additional tooling to track. Without this, it can be difficult to manually track the use of data in a system. However the problem is, that  this correction model has created a system dependency on the actual model, making it significantly more expensive to analyze improvements to that model in the future. 

    Correction Cascades:
    There are situations in which a problem for a model exists, but a solution for a slightly different problem for another model is required. As a solution, it can be useful to learn the other model and take it as input and learn a small correction. It can become even more problematic if the correction model is cascaded, because it will create a situation where improving the accuracy of the actual model actually leads to system-level detriments and deadlocks.


    System-level Spaghetti:
    The development of self-contained packages can create a massive amount of supporting code which is written to get data into and out of general-purpose packages. This is called Glue Code and can be costly in the long term, as it tends to freeze a system to the peculiarities of a specific package. A special case of glue code are pipeline jungles which often appears in data preparation and can evolve organically, as new signals are identified and new information sources added. The risk with this pattern is that it can become a jungle of scrapes, joins, and sampling steps, often with intermediate files output. As a result, managing these pipelines, detecting errors and recovering from failures are all difficult and costly and testing such pipelines often requires expensive end-to-end integration tests. As an attempt at a solution to the hardening of glue code or pipeline jungles performing experiments with alternative algorithms or tweaks by implementing these experimental codepaths as conditional branches within the main production code are performed. However, over time, these accumulated codepaths can create a growing debt. Maintaining backward compatibility with experimental codepaths is a burden for making more substantive changes. Furthermore, obsolete experimental codepaths can interact with each other in unpredictable ways, and tracking which combinations are incompatible quickly results in an exponential blowup in system complexity. 

    Dealing with changes in the external world:

## What are the credentials of the authors with regard to machine learning? Have they published research on machine learning (or using machine-learning techniques) previously?








## Papers

[1] Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., ... & Young, M. (2014). Machine learning: The high interest credit card of technical debt.
