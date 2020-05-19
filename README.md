# AZNG_Projects (Beta)
A repository of tools used at Local FCs, built by the same associates that work in them. These are the Beta releases and may have Critical bugs that can impact work; Only use in a controlled environment or where error is not a problem.

## Layout

This repository will be maintained in a clean, however, ever changing layout. Current layout will be comprised such that the downloaded file will extract as...

AZNG/Applications  >> Contains all the individual applications; AIO release will be structured differently
AZNG/Assets  >> Containing images or other art assets used by files
AZNG/Data  >> Contains configuration files, or junk files to enable betas
AZNG/Temp  >> Directory should not have files placed in it in the Repo, but for when apps are being updated to ensure safe movement

## Programs

* AZNG Launcher
* BinScraper
* PodBuilder
* Updater
* Setup

### AZNG Launcher

This application serves as the main launcher for FC associates. It will launch a session related to the role they have selected and provide them with the corrisponding or most relevent Labor Tracking code. This launcher relies on internal Amazon links and is not suitable for external uses without modification.

### BinScraper

This application scrapes bin labels from an FC Research session. It must be able to intake 2 specific formats and back test both at all times. The end result is a list of printable bin labels. This is suitable for "item hunt" sessions.

### PodBuilder

Pod Builder is a standalone application that is meant to work with Pod console in an effort to virtully build pods. It requires a recipe card that is only available on a physically present pod skin. Should the card be missing, this application will prove inneffective.

### Updater

The application responsible for retrieving application updates and downloading new applications if available via an update file.

### Setup

etup is responsible for retrievable a link file that contains internal Amazon links; The application is unable to retrieve this file without a special physical card only given to associates.
