## QA Workshop 2 sample code

This repository contains the code that we wrote during the second QA workshop.

It uses pytest to run playwright end to end tests.

There is a GitHub actions CI that runs the tests against the deployed version of: https://automation-workshop.hacksoft.io/admin/ (repository: https://github.com/HackSoftware/qa-workshop)

The code is reading the envs from the `.env` file. Look at at `.env.example`.

It also uses the `/nuke` api to nuke the database before every run. 