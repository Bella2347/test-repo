# Description

## Background

[Link to Teams task]()

*Describe the background to the change.*

## Changes

*Text under this header will be copied to EventLog on merge.*

*Describe in detail the changes made. If relevant mention steps, workflows etc.*

### Config-slicer

Configuration backed up with config-slicer: */opt/cmd/config_slices/file_name*

## Test plan

*Describe the testplan and if the requestor or other personnel is involved. If requirements or test cases have been updated, link to requirements and test cases or write name and ID of test cases.*

*[New requirement]()*

*[Updated test case]()*

# Checklist

## Before review

- [ ] Add label indicating size: *Tiny/Small/Medium/Large* (add *Issue* when applicable)
- [ ] Configuration backed up with config-slicer (if needed)
- [ ] Requirements checked (created/updated if needed)
- [ ] Testcases checked (created/updated if needed)
- [ ] Tests (regression and acceptance) passed on test server
- [ ] Pytests passed (folder tests)
- [ ] Merge master to branch

## After review

- [ ] Merge master to branch (incase changes have been made)
- [ ] Smoketests passed on production server
- [ ] Squash and merge PR
- [ ] Delete branch
- [ ] Pull changes to live on the production server
- [ ] Pull changes to live on the test server
