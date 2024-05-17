# Playwright 
Repo for using Playwright as our test framework. This is our location for UI Integration tests and end to end tests, replacing the UI test portion within Pegasus. Playwright is a framework created by Microsoft which has rich features for testing, debugging and reporting. 

## Install
1. Setup Toolbox https://github.com/DexCare/toolbox#machine-setup
2. You need to run: 
- `nvm use` to switch to the proper version of Node (16.10)
- `npm install` to install dependencies 
- `npx playwright install` to install playwright's browsers matching with the installed ones.
3. Review https://dexcare.atlassian.net/wiki/spaces/TES/pages/18179588097/How+to+install+and+use+Playwright for more info.

## Execute
To run the tests using Playwright command
```bash
npx playwright test
```
### To run a subset of tests by tag
```bash
NODE_ENV=kp npx playwright test test/kp/kp_virtual_test.spec.ts
```
```NODE_ENV``` is needed for the tests to know which Config files to use. Located under ```config/env/[customer].json``` These files contain URL's and customer specific variables that tests use at runtime.

### To run any of the predetermined test targets: 
```npm run kp-uat```
To debug locally, run a subset of tests and edit ```playwright.config.ts``` and change reporter: to ```'html'```. Otherwise the output will be sent to testrail. 
If you wish to run headed vs headless, change playwright.config.ts ```headless: true/false```. Be sure to change it to true before committing for CI/CD purposes.
You can also use the ```--headed``` arg through the CLI.


## Creating tests and Synching to TestRail
1. Test your workflow manually, be mindful of the test data you use, can this be reproduced over and over by an automated test? Is the test user you're using used in many other tests? What can cause this test to be flaky?
2. Create the test in TestRail https://dexcare.testrail.io/index.php?/suites/overview/22. 
  a. Select an appropriate test suite
  b. Make a subsection if necessary or stick your test in any of the exisiting subsections.
  c. Create a test and make sure you fill in Description, Is Automated?, Automation Type, Customer and add Steps. These help with reporting and if Steps and Description is not added, your code will fail to write to TestRail
  d. Grab testCase ID from testrail after you create the test, EX: "C12345". 
3. Write your test in Playwright, in the name of the test, include the testrail Id as ```@C12345``` in the name. This is necessary for the test to be picked up by TestRail through our customer testrail_reporter located in the codebase. Write steps within your test, follow examples using test.step().
4. Make sure your test passes locally. Change reporter in ```playwright.config.ts``` back to our custom testrail_reporter and make sure results for your tests accurately appear in TestRail, for example like this: https://dexcare.testrail.io/index.php?/runs/overview/22. (There is a Test Rails Reviewer account in 1Pass that you can use to login and see your test cases results in test rails)

## Suggestions for Running Locally
1. In ```playwright.config.ts``` change headless value to  ```false```  to more easily debug.
2. Change ```reporter``` value from our custom testrail reporter to the html reporter for easier debugging.
3. Change `retries` to `process.env.CI ? 2 : 0` for running a failing test only once.
4. Validate that your test syncs to testrail correctly in passing and failing state by switching reporter back to the testrail reporter.
5. Do NOT stage your local changes to `playwright.config.ts`
6. Create PR

## Known Bugs
Some test failures may be due to known bugs, clone the following ticket: https://dexcare.atlassian.net/browse/ENG-3473

## Other Issues
run
>npm install --save-dev @types/testing-library__jest-dom
with errors like: Property 'toBeChecked' does not exist on type 'Matchers<void, Element>' 

## Mock API with Playwright
Mock API supports:
1. Mock API requests
2. Modify API responses
3. Mocking with HAR file
   1. Recording a HAR file
   2. Modifying a HAR file
   3. Replaying from HAR

Playwright official document about Mock API: https://playwright.dev/docs/mock

A easy to understand wiki with good examples: https://blog.delpuppo.net/playwright-mock-api

More about HAR: https://playwright.dev/docs/api/class-page#page-route-from-har


## RAF & GPOM
RAF - Rose's Automation Testing Framework: https://dexcare.atlassian.net/l/cp/gLZpLpCu
GPOM - Generic Page Object Model: https://dexcare.atlassian.net/l/cp/gLZpLpCu
Playwright script in RAF with GPOM example(Retail E2E Flow): https://dexcare.atlassian.net/l/cp/fZc31q1r

Test run control is implemented by calling 
    const result = await ConfigUtils.shouldRun(testCaseConfig);
    test.skip(!result.shouldRun, result.reason);
for each describe/test. 

To audit the test cases are compliant with RAF test run control,  
> npm run audit:testrun
All the tests are expected to be skipped without running any command.

## node-config-ts 
It will support multiple config files from 3.3.9(https://github.com/node-config/node-config/pull/486/commits/a27b95993a06dfb66582b32252416597ae20f6d0). 
Since right now only one file is allowed, the urls of QA-tier will temporarily stays in user config files.

## quickly get some patient in virtual queue
> NODE_ENV=frosh DEPLOYMENT=testrun.data.gen npx playwright test tests/gpom/gendata/virtualbooknocancellation
NODE_ENV can be set to any environment like thr-uat
or run any spec file in the folder for different flow like
> NODE_ENV=frosh DEPLOYMENT=testrun.data.gen npx playwright test tests/gpom/gendata/virtualbooknocancellation/booking_flow_new_patient.spec.ts

## TestRail Reporting

If you want to use the TestRail reporter, you first need to have a TestRail account.

#### Environment Variables
To configure TestRail reporting, set the following environment variables via the command line or update in [`testRail.config.ts`](#configuring-testRail-reporting) file:

1. `REPORTER`: In order to run in TestRail set "testRail". $\color{red}{*}$
2. `TR_USER`: User email for TestRail, can also be updated in a `testRail.config.ts` file. $\color{red}{*}$
3. `TR_PASS`: User password for TestRail, can also be updated in a `testRail.config.ts` file. $\color{red}{*}$
4. `TR_SUITE_ID`: Suite ID, by default [34](https://dexcare.testrail.io/index.php?/suites/view/34).
5. `RUN_ID`: Run ID to reuse a specific run.
6. `TR_NAME`: Prefix for the run name: `<TR_NAME> - <CurrentDate> - <browser> - Automation - <Customer>`.
7. `VERSION`: Suffix for the run name: `<CurrentDate> - <browser> - Automation - <Customer> - <VERSION>`.
8. `NEW_RUN`: To create a new run, by default `false`

####  Configuring TestRail reporting
   1. `testRail.config.ts` file located in `playwright-ui-tests/src/utils/`: TestRail configuration details such as the host  URL, username, password, projectId, customer, runId, suiteId, testRunName, reporter, version, createNewRun.
        
   2. `testrail_reporter.ts ` file located in `playwright-ui-tests/src/utils/`:  Implementation for integrating TestRail reporting into a testing framework.

#### TestRail Execution Commands

> To create or reuse a run in TestRail, use the following command (this command reuses an existing TestRail run if it already exists, otherwise, it creates a new TestRail run.):
``` bash
REPORTER=testRail TR_USER=<username> TR_PASS=<password> NODE_ENV=frosh npx playwright test <path> 
```

> To reuse a specific run
 ``` bash
REPORTER=testRail RUN_ID=<runId> TR_USER=<username> TR_PASS=<password> NODE_ENV=frosh npx playwright test <path> 
```

> To create a new run
 ``` bash
REPORTER=testRail NEW_RUN=true TR_USER=<username> TR_PASS=<password> NODE_ENV=frosh npx playwright test <path> 
```
or 
 ``` bash
REPORTER=testRail TR_NAME=<prefix> TR_USER=<username> TR_PASS=<password> NODE_ENV=frosh npx playwright test <path> 
```
#### TestRail reporting via GHA

You can create and reuse TestRail runs using GitHub Actions (GHA). Follow these steps to report in TestRail via GitHub Actions workflow:

1. **Navigate to Repository**: Open the `playwright-ui-tests` repository on GitHub.

2. **Access Actions Tab**: Navigate to the "Actions" tab.

3. **Select Workflow**: Choose the proper workflow (e.g.,`daily e2e frosh test cases`).

4. **Create/reuse Run**:
   - Click on the Run workflow button
   - By default, this will run on the main branch. If you want to change it, select the branch for which you want to create or update the TestRail run.
   - To create a new TestRail run you can provide a run name prefix, by default it will be `Daily E2E UI Booking`.
   - To reuse an already created run in TestRail uncheck the 'Create a new TR run?' option.
   - Click on the "Run workflow" button.
