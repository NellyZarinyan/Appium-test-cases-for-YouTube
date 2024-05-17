#### Environment Variables
To configure TestRail reporting, set the following environment variables command line or in `testRail.config.ts` file:

1. `REPORTER`: In order to run in TestRail set "testRail" $\color{red}{*}$.
2. `TR_USER`: User email for TestRail, can also be updated in a `testRail.config.ts` file.
3. `TR_PASS`: User password for TestRail, can also be updated in a `testRail.config.ts` file.
4. `TR_SUITE_ID`: Suite ID, by default `34`.
5. `RUN_ID`: Run ID, by default `0`.
6. `TR_NAME`: Prefix for the run name: `<TR_NAME> - <CurrentDate> - <workerName> - Automation - <Customer>`.
7. `VERSION`: Suffix for the run name: `<CurrentDate> - <workerName> - Automation - <Customer> - <VERSION>`.
8. `NEW_RUN`: Set `true` to create a new run, by default `false`

$\color{green}{test}$
