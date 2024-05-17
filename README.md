#### Environment Variables
To configure TestRail reporting, set the following environment variables command line or in `testRail.config.ts` file:

1. `REPORTER`: In order to run in TestRail set "testRail" $${\color{red}*}$$.
2. `TR_USER`: User email for TestRail, can also be updated in a `testRail.config.ts` file.
3. `TR_PASS`: User password for TestRail, can also be updated in a `testRail.config.ts` file.
4. `TR_SUITE_ID`: Suite ID, by default `34`.
5. `RUN_ID`: Run ID, by default `0`.
6. `TR_NAME`: Prefix for the run name: `<TR_NAME> - <CurrentDate> - <workerName> - Automation - <Customer>`.
7. `VERSION`: Suffix for the run name: `<CurrentDate> - <workerName> - Automation - <Customer> - <VERSION>`.
8. `NEW_RUN`: Set `true` to create a new run, by default `false`


#### Required Environment Variable: `NODE_ENV` <span style="color:red">＊</span> #f03c15

Make sure to set the `NODE_ENV` environment variable to specify the environment configuration.
- ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) `#f03c15`
- ![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) `#c5f015`
- ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `#1589F0`
