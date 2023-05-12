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
                some strategies may help but its also means that shipping the first version of a machine learning system is easy, but that making subsequent improvements is unexpectedly difficult.
## What are the credentials of the authors with regard to machine learning? Have they published research on machine learning (or using machine-learning techniques) previously?








## Papers

[1] Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., ... & Young, M. (2014). Machine learning: The high interest credit card of technical debt.
