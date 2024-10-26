# TrueNas Apprise API Adapter

TrueNas does not natively provide a way to send alerts and notifications to an Apprise API server. This repo 'abuses' the TrueNas Slack alert integration and provides a fake slack webhook endpoint to forward alerts to an Apprise API server.
Note that Slack is not required at all for this integration to work.

## Installation
1. Apps -> Discover Apps -> Custom App
    - Enter an Application Name, e.g. "truenas-apprise"
    - _Image Repository_: ghcr.io/tieum/truenas-apprise-adapter
    - _Image Tag_: main
    - Environment Variables:
        - _Name_: APPRISE_URL
        - _Value_: [your apprise url] e.g.https://apprise.example.com/
        - _Name_: APPRISE_CONFIG_ID
        - _Value_: [your apprise config id] e.g. aabbccddeeff1122334455
        - _Name_: APPRISE_TAG
        - _Value_: [the apprise tag you want to send alerts ] e.g. signal

    - Check _"Provide access to node network namespace for the workload"_
    - Save

1. System Settings -> Alert Settings -> Add
    - _Type_: Slack
    - _Webhook URL_: http://localhost:12345
    - Click _Send Test Alert_ to test the connection
    - Save
