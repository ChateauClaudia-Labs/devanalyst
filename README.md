# devtools

The `devtools` package provides support for data-driven analysis of a software development's team efficiency.
At present it provides support for:
- Simulation of a release cycle:
  - User story burndown
  - Buf inflow
- Analysis of GIT logs
  - Ingest of data
  - Inference of user story associations for properly commented GIT commits
  - Creation of a datamart
  - Metrics around identifying where the volatility lies
  - Metrics around interference

In the future it is planned to provide support as well for:
- Simulation of a release cycle:
  - Source commits
- JIRA support
  - Ingest of data to datamart
  - Linkage to datamart entries processed by ingesting GIT logs
- Efficiency metrics
  - More thorough common model for the data inputs associated to a release cycle
  - Mathematical definition of efficiency metrics
- More data analysis
  - Ability to validate or refute efficiency hypothesis
  - Hotspotting to pin down inefficiency drivers in the code or the team
