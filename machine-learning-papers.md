# Questions about Machine Learning Papers

## What are some common use cases for machine learning in practical applications or research prototypes?

[1] According to Sculley et al., the most important reason for using a machine learning system is that "the desired behavior cannot be
effectively implemented in software logic without dependency on external data".

According to Kostakos & Musolesi (2017) one common use case for machine learning is activity recognition for example in wearable computing or other user interaction techniques like gesture recognition. It is also used to optimize system resources one example here is the optimization of battery conservation. Another use case is to provide intelligent mobile notifications to the users.

Especially in research Kostakos & Musolesi (2017) identify machine learning is used to model human behavior. Another research topic using machine learning is the prediction of future user activities and interactions.


## Which problems of machine learning do the authors of the papers identify?

One problem according to Kostakos & Musolesi (2017) is that the inner workings of machine learning models are not transparent. This problem is especially prevalent when generating new knowledge about the world and when using unsupervised learning. The authors argue that in these cases preliminary testing bevor adopting machine learning techniques is necessary. 

Another problem the authors identify is that machine learning algorithms give insight only in association relationships and not causality, because of this one must be extremely careful when extrapolating conclusions. They argue further that this problem is even more prominent when using data collected through crowdsourcing and not collected it in an experimental setting.

Another problem is the interpretation of accuracy reported for machine learning algorithms. The accuracy always should be interpreted considering the task solved. This gets obvious comparing a classifier with tow classes and a classifier with 16 different classes, because the first one has a random baseline of 50 percent and the second one has a baseline of only 6.6 percent. So, in this case 85 percent accuracy would be much better for the second algorithm. Its also should be considered that we maybe do not expect a random baseline for a task.

The last problem identified by Kostakos & Musolesi (2017) is when machine learning techniques are applied to subsets of data, because this results in only capturing a limited part of the phenomena.

[1] On the meta level, Sculley et al. list the technical dept as the main problem that can arise as a result of using machine learning concepts. 

The Term "Technical Dept" was introduced by Ward Cunningham in 1992 [2] as a way to help quantify the cost of moving quickly to ship new
products or services in context of software engineering. 
    
Technical dept can cause the following three main problems:

  - massive ongoing maintenance costs at the system level
  - system brittleness
  - reduced rates of innovation

   According to Sculley et al. this main problems in context of machine learning are caused through...

        - machine learning packages have all the basic code complexity issues as normal code, but also have a larger system-level complexity that can create hidden debt. 
          Thus, refactoring these libraries, adding better unit tests, and associated activity is time well spent but does not necessarily address debt at a systems level.
        - subtly erosion of the abstraction boundaries at a system-level.
        - creation of unintended tight coupling of otherwise disjoint systems through re-use of input signals.
        - large masses of “glue code” or calibration layers that can lock in assumptions because machine learning treated as black boxes
        - changes in the external world may make models or input signals change behavior in unintended ways.

    
    The causes for this problems can be divided into the following categories:

    Entanglement: 
                Machine learning models are machines for creating entanglement and making the isolation of improvements effectively impossible. This leads to changing anything leading to changing everything (CACE principle). As a result of such changes the prediction behavior may alter, either subtly or dramatically, on various slices of the distribution. To take entanglement some strategies may help but its also means that shipping the first version of a machine learning system is easier, but in reverse subsequent improvements are unexpectedly difficult.

    Hidden Feedback Loops: 
                Machine learning models as systems that learn from world behavior are clearly intended to be part of a feedback loop. Hidden feedback loops arises through ongoing feature adjustments and new data updates on the machine learning model. This causes the system just slowly changing it prediction behavior. Gradual changes not visible in quick experiments make analyzing the effect of proposed changes extremely difficult, and add cost to even simple improvements.

    Undeclared Consumers:
                Making predictions from a machine learning model accessible to other systems can cause a visibility debt. Which means that without access controls, it is possible for some of these consumers to be undeclared consumers, consuming the output of a given prediction model as an input to another component of the system. 

    Unstable Data Dependencies:
                The consumtion of signals as input features that are produced by other systems has the potential risk that some input signals are unstable, meaning that they qualitatively change behavior over time. As a result, changes and improvements to the input signal may be regularly rolled out, without regard for how the machine learning system may be affected. This causes input signals to may have arbitrary, sometimes deleterious, effects that are costly to diagnose and address.

    Underutilized Data Dependencies:
                That is understood to mean packages that are mostly unneeded and are costly, since they make the system unnecessarily vulnerable to changes. Underutilized dependencies can creep into a machine learning model in several ways like for example legacy features or bundled features.

    Static Analysis of Data Dependencies:
                One of the key issues in data dependency debt is the difficulty of performing static analysis, because it requires additional tooling to track. Without this, it can be difficult to manually track the use of data in a system. However the problem is, that  this correction model has created a system dependency on the actual model, making it significantly more expensive to analyze improvements to that model in the future. 

    Correction Cascades:
                There are situations in which a problem for a model exists, but a solution for a slightly different problem for another model is required. As a solution, it can be useful to learn the other model and take it as input and learn a small correction. It can become even more problematic if the correction model is cascaded, because it will create a situation where improving the accuracy of the actual model actually leads to system-level detriments and deadlocks.

    System-level Spaghetti:
                The development of self-contained packages can create a massive amount of supporting code which is written to get data into and out of general-purpose packages. This is called Glue Code and can be costly in the long term, as it tends to freeze a system to the peculiarities of a specific package. A special case of glue code are pipeline jungles which often appears in data preparation and can evolve organically, as new signals are identified and new information sources added. The risk with this pattern is that it can become a jungle of scrapes, joins, and sampling steps, often with intermediate files output. As a result, managing these pipelines, detecting errors and recovering from failures are all difficult and costly and testing such pipelines often requires expensive end-to-end integration tests. As an attempt at a solution to the hardening of glue code or pipeline jungles performing experiments with alternative algorithms or tweaks by implementing these experimental codepaths as conditional branches within the main production code are performed. However, over time, these accumulated codepaths can create a growing debt. Which means that maintaining backward compatibility with experimental codepaths is a burden for making more substantive changes. Furthermore, obsolete experimental codepaths can interact with each other in unpredictable ways, and tracking which combinations are incompatible quickly results in an exponential blowup in system complexity. 

    Dealing with changes in the external world:
                One approach to deal with changes in the external world data is to choose a threshold from a set of possible thresholds, in order to get good tradeoffs on certain metrics, such as precision and recall. As a result such thresholds are often manually set. Thus if a model updates on new data, the old manually set threshold may be invalid. This fixed thresholds in dynamic systems create the need to manually update many thresholds across many models, which is time-consuming and brittle. Another problem is when correlations no longer correlate. This problem occures when machine learning systems have a difficulties distinguishing the impact of correlated features. Finally, when it comes to unit testing of individual components and end-to-end tests of running systems, such tests are not sufficient to provide evidence that a system is working as intended. As a result, making live monitoring of system behavior in real time critical.



## What are the credentials of the authors with regard to machine learning? Have they published research on machine learning (or using machine-learning techniques) previously?

Both authors have published about machine learning. Some examples for Vassilis Kostakos are [3, 4]. Mirco Musolesi also have papers about this topic published [5, 6].
Looking at Sculley D. research history it's not his first research paper on machine learning and specifically not his only paper about problems in machine learning. He contributed in severel papers to the research of challenges in machine learning and specifically about the hidden technical dept aspect of machine learning (for example [7, 8, 9, 10]). 






## Papers

[1] Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., ... & Young, M. (2014). Machine learning: The high interest credit card of technical debt.

[2] Cunningham, W. (1992). The WyCash portfolio management system. ACM SIGPLAN OOPS Messenger, 4(2), 29-30.

[3] Van Berkel, N., Luo, C., Anagnostopoulos, T., Ferreira, D., Goncalves, J., Hosio, S., & Kostakos, V. (2016, May). A systematic assessment of smartphone usage gaps. In Proceedings of the 2016 CHI conference on human factors in computing systems (pp. 4711-4721).

[4] Sharma, K., Niforatos, E., Giannakos, M., & Kostakos, V. (2020). Assessing cognitive performance using physiological and facial features: Generalizing across contexts. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, 4(3), 1-41.

[5] Mikelsons, G., Smith, M., Mehrotra, A., & Musolesi, M. (2017). Towards deep learning models for psychological state prediction using smartphone data: Challenges and opportunities. arXiv preprint arXiv:1711.06350.

[6] Darvariu, V. A., Convertino, L., Mehrotra, A., & Musolesi, M. (2020). Quantifying the relationships between everyday objects and emotional states through deep learning based image analysis using smartphones. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, 4(1), 1-21.

[7] Ovadia, Y., Fertig, E., Ren, J., Nado, Z., Sculley, D., Nowozin, S., ... & Snoek, J. (2019). Can you trust your model's uncertainty? evaluating predictive uncertainty under dataset shift. Advances in neural information processing systems, 32.

[8] Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., ... & Dennison, D. (2015). Hidden technical debt in machine learning systems. Advances in neural information processing systems, 28.

[9] D'Amour, A., Heller, K., Moldovan, D., Adlam, B., Alipanahi, B., Beutel, A., ... & Sculley, D. (2022). Underspecification presents challenges for credibility in modern machine learning. The Journal of Machine Learning Research, 23(1), 10237-10297.

[10] Smilkov, D., Thorat, N., Assogba, Y., Nicholson, C., Kreeger, N., Yu, P., ... & Wattenberg, M. M. (2019). Tensorflow. js: Machine learning for the web and beyond. Proceedings of Machine Learning and Systems, 1, 309-321.
