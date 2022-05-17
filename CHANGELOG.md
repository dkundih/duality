CHANGELOG 
==========

**as alunari**

0.0.1 (16/08/2021)
- initial release.

0.0.2 (16/08/2021)
- reupload for functionality.

0.0.3 (16/08/2021)
- README update.
- LICENSE update.
- stability downgrade to 4 - Beta in order to provide more testing and feedback.

0.0.4 (17/08/2021)
- minor README update.
- functionality confirmed in testing environment (Visual Studio Code, PyCharm, JupyterLab, Google Colab).

0.0.5 (23/08/2021)
- minor README update with Documentation link changed.

1.0.0 (28/08/2021)
- first stable release.
- major functionality changes.
- reworked 2 functions (.stats is now .get_stats, .risk is now .get_risk).
- added 1 new function (.get_change).
- .documentation updated.
- .montecarlo.functions updated.
- developement status is now 5 - Production/Stable.

1.0.1 (28/08/2021)
- small repository update.

1.0.2 (28/08/2021)
- LICENSE website change.
- updated information in the functions.

1.1.0 (30/08/2021)
- README update.
- alunariTools class created to distinguish logistics tools and functions from original montecarlo class.
- created a counter of iterations to track live progress.

1.1.1 (31/08/2021)
- now requires alunariTools in order to provide less confusing code, done outside of the original function.

1.1.2 (09/09/2021)
- confirmed functionality in Sublime Text.
- added __name__ == '__main__' info.
- minor README update.

1.1.3 (10/09/2021)
- redefined documentation.

1.1.4 (13/09/2021)
- improved user experience and stability.

1.1.5 (13/09/2021)
- typo corrections.

1.1.6 (19/09/2021)
- adjustments to montecarlo.execute() following the dependency changes of alunariTools package.
- stability and functionality confirmed in repl.it environment.

1.1.7 (19/09/2021)
- dependencies bug fix.

1.1.8 (19/09/2021)
- upload bug fix.

1.1.9+ (22/09/2021)
- merge test.

1.2.0 (22/09/2021)
- alunari and alunariTools are now merged into alunari. Former alunariTools functions are now called with alunari.essence.

1.2.1+ (24/09/2021)
- EOQ setup test.
- montecarlo class is now Configuration.

1.3.1 (25/09/2021)
- major rework and functionality update.
- code structure redifined.

1.3.2 (26/09/2021)
- code structure redifined.

1.3.3 (26/09/2021)
- cleaner and better defined code.
- partial imports from the library instead of whole modules applied.

1.3.4 (26/09/2021)
- minor bug fix.

1.3.5 (27/09/2021)
- alunari.montecarlo.Configuration().get_risk() now works independently with it's unique simulation counter that is set to 5000 by default.
- alunari.montecarlo.Configuration.help() updated to match the changes made to the function.

1.3.6 (27/09/2021)
- dependencies updated to meet repl.it requirements.

1.3.7 (29/09/2021)
- Configuration function now prints the confirmation of the simulation set up.

1.3.7+ (11/10/2021)
- redefined hist() function test.

**as vandal**

0.0.1 (03/10/2021)
- initial release.

0.0.2 (03/10/2021)
- vandal replaces the functionality of the currently discarded alunari python package.

1.1.0 (11/10/2021)
- redefined code of .hist() function.
- added event log that tracks the execution time and duration of functions.

1.1.1 (11/10/2021)
- log tracking now applies on all relevant class functions.

2.0.0 (11/10/2021)
- vandal transcedents alunari versions by becoming v2+

2.0.1 (12/10/2021)
- minor tweaks to CHANGELOG and README
- .help() now properly shows requirements of .get_logs() function.

2.0.2+ (12/10/2021)
- photo added to the header.

2.0.3 (12/10/2021)
- confirmed stabile version after test.

2.1.0 (12/10/2021)
- republished.

2.1.1 (13/10/2021)
- replaced alunari with vandal where it was initially missed out.
- now propely applies highly fragmented dataframe warning removal for simulations over 102.

2.1.2 (13/10/2021)
- stability update.

2.1.3 (22/10/2021)
- EOQ implementation.
- vandal.essence renamed to vandal.hub.
- this is an unstable version that has yet to be tested.

2.2.0 (22/10/2021)
- confirmed stability.

2.2.1 (22/10/2021)
- README and flexibility update.

2.2.2 (28/10/2021)
- now properly shows CHANGELOG of discarded alunari package.

**as duality**

3.0.0 (03/11/2021)
- initial release
- now properly shows CHANGELOG of vandal package history.

3.0.1 (04/11/2021)
- code tweaks.

3.1.1 (06/11/2021)
- MonteCarlo and EOQ now automatically perform .execute() function.
- MonteCarlo.hist() now executes get_stats() alongside to get info about standard deviation.
- MonteCarlo and EOQ are now being imported as objects.
- global_functions removed and merged into meta folder.

3.1.1+ (06/11/2021)
- functionality tests.

3.1.2 (06/11/2021)
- complete redesign pushed to public.

3.1.3 (06/11/2021)
- initial import now imports hub module as well as associated contents in order to enable print(help(duality.hub)) function.

3.1.4 (07/11/2021)
- updated README.

3.1.5 (08/11/2021)
- untracked changes.

3.1.6 (12/11/2021) - not useable.
- code cleanup in hub and montecarlo modules.

3.1.7 (12/11/2021)
- quick bug fix.

3.1.8 (12/11/2021)
- sync with recent GitHub changes.

3.1.9 (13/11/2021)
- README style update.

3.2.0 (13/11/2021)
- return_data = True added into MonteCarlo object for decision of the time of execution manually.

3.2.1 (14/11/2021)
- setup.py redefined with metadata.

3.2.2 (17/11/2021)
- regular maintainance.

3.3.0 (19/11/2021) - UNSTABLE
- package now becomes a library.
- DEVELOPER MODE introduced.
- disables @classlog functions outside of DEVELOPER MODE.
- code readability improved.
- duality.hub.hub is now duality.hub.toolkit.
- eoq and montecarlo folders merged into objects folder.
- added support for import __all__ contents of a module.

3.3.2 (19/11/2021) - UNSTABLE
- republish and 3.3.1 ghost overwrite.

3.3.3 (20/11/2021) - UNSTABLE
- initial bug fix deployed.

3.3.4 (20/11/2021) - UNSTABLE
- additional bug fixes deployed.

3.3.5 (20/11/2021) - UNSTABLE
- additional bug fixes deployed.
- code readability improved.

3.3.6 (20/11/2021)
- confirmed functionality and stability.

3.3.7 (20/11/2021)
- code reconstruction.

3.4.0 (22/11/2021)
- NEW FEATURE: duality.Dijkstra algorithm.

3.4.1 (22/11/2021)
- minor code cleanup.

3.4.2 (22/11/2021)
- functionality confirmed.

3.4.3 (22/11/2021)
- upstream/downstream fix.

3.4.4 (01/12/2021)
- CLI environment setup.

3.5.0 (01/12/2021)
- CLI environment tests.
- demonstration repository now merged into duality.
- MonteCarlo, Dijsktra and EOQ no longer define the data, data config shifted to .execute() function of every object.
- CLI can now be executed in teminal using 'duality.__main__' for IDE or 'python __main__.py' for CMD or Powershell after locating with cd.
- stability of 3.5. series will not be guaranteed, it is a transitional phase for future integrations into applications and web applications.

3.5.1 (01/12/2021)
- CLI environment tests.
- code readablity improved.

3.5.2 (01/12/2021)
- CLI environment tests.
- dualityCLI integration into the source.
- CLI contents added into __all__ and __init__ files.

3.5.3 (01/12/2021) - UNSTABLE
- first functional CLI for MonteCarlo imlpemented.
- added saving to .csv, .xlsx and .json for out-of-terminal functions.

3.5.4 (01/12/2021) - UNSTABLE
- active tests.

3.5.5 (01/12/2021) - UNSTABLE
- bug fixes.

3.5.6 (01/12/2021)
- functionality resolved using pypyxl.
- duality.dualityCLI and python __main__.py now officially work.

3.5.7 (01/12/2021)
- added block = False to plt.show() in order to unlock further actions after a graph in dualityCLI.

3.5.8 (01/12/2021) - UNSTABLE
- cli code redefined and made user friendly.
- dualityCLI is not CLI.

3.5.9 (01/12/2021) - UNSTABLE
- now contains the executable CLI file with .exe extension within CLIexe folder.
- dualityCLI.exe v1.0 functionality equalized with 3.5.9 version of python __main__.py and duality.CLI()

3.5.10 (01/12/2021) - UNSTABLE
- dualityCLI.exe release postponed, use python __main__.py or duality.CLI() to execute.

3.5.11 (01/12/2021)
- dualityCLI.exe files removed from the package.
- CLIexeversion is now CLIversion.

3.5.12+ (02-03/12/2021)
- CLI v1.1 version replaces the CLI v1.0
- added menu and help actions to Dijkstra and EOQ until they become implemented.
- bugfix of MonteCarlo simulations being period and vice versa.

3.6.1 (03/12/2021) - STABLE
- CLI v1.21 version added.
- CLI stable after initial tests.

3.6.2 (04/12/2021) - STABLE
- CLI v1.22 version added.
- colored CLI functions.
- colorama added to dependencies.
- added clear screen after exiting clients.

3.6.4 (04/12/2021)
- skips ghost 3.6.3 version.
- CLI v1.23 version added.
- quick bugfix of executing greet() after cls in CLI.

**as duality**

4.0.0 (27/12/2021)
- previous versions of duality library transfered into the vandal package.
- duality is now a decorator package for vandal package.

4.1.0 (28/12/2021)
- added dictionary, basic and descriptive display menus.
- display now also executes the function that it is decorating.
- added various options to functions (style, method, return_option).

4.1.1 (28/12/2021)
- ignores pycache from forming in directories.

4.1.2 (28/12/2021)
- confirmed functionality of the package.

4.1.3 (28/12/2021)
- matches newest vandal framework changes.

4.1.4 (07/01/2022)
- redefined dictionary option to serve as an executeable menu.
- redefined the appearance of functions in JSON format.

4.1.5 (07/01/2022)
- record.config function added as a CLI creation particle.
- redefined docstrings for easier use.

4.1.6 (07/01/2022)
- record.config is now record.static_config.
- added record.dynamic_config that loops the record.static_config.

4.1.7 (07/01/2022)
- reverted 4.1.6 changes.

4.1.8 (08/01/2022)
- Meta class added to make class object instances available.

4.1.9 (08/01/2022)
- Meta included in init.

4.1.10 (08/01/2022)
- code cleanup.

4.1.11 (25/01/2022)
- code redefinition.
- record and track are now stored in different modules.
- classparticles module removed.
- track is now marked as DEPRECATED due to structural difficulties.

4.1.12 (25/01/2022)
- no longer requires vandal.

4.1.13 (31/01/2022)
- now also supports execution within class methods with self parameter.

4.1.14 (01/02/2022)
- now also includes a customizable headline option for the menu.

4.1.15 (02/02/2022)
- now properly enables quit function by forcing self function execution first.

4.2.0 (02/02/2022)
- added type option to config in order to execute properly on both static and dynamic functions and methods.

4.2.1 (06/03/2022)
- regular maintenance.

4.3.0 (13/03/2022)
- improved code readability.

4.3.1 (14/03/2022)
- dict defined as dict[str, str].

4.3.2+ (22/03/2022) - UNSTABLE
- tests.

4.4.2 (23/03/2022)
- confirmed fucntionality of deployed changes.
- cleaner and more organized code.
- now also imports meta data.
- uses the scheme of vandalTypes for datatypes.

4.4.3 (27/03/2022)
- queue options set to test.

4.4.4 (27/03/2022)
- prerequisites for app put to test in real time environment.

4.4.5 (27/03/2022)
- now fetches the vandalTypes from vandal.
- __all__ functions redefined to string.
- vandal >= 3.7.0 dependency added.

4.4.6 (28/03/2022)
- confirmed functionality.
- vandal upgrade.
- .testassets files updated.

4.5.0 (30/03/2022)
- autoinit option implemented to entry.
- contains_autoinit added to config.

4.5.1 (30/03/2022)
- now automatically recognizes if any of the functions contains autoinit.
- Record.define(input_val, dtype) introduced to pass arguments as inputs.
- UX improved.
- vandal >= 3.7.2 dependency to fetch AnyType.

4.6.0 (18/05/2022)
- implemented store function that stores function arguments as inputs of a certain data type.
- show_dtypes added to config.