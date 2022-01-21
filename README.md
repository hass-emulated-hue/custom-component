# emulated-hue-integration

[![GitHub Release][releases-shield]][releases]
[![hacs][hacsbadge]][hacs]

## What

This simply exposes ESPHome device IPs using the Home Assistant API at `/api/config/esphome/entries`.

This allows Hass Emulated Hue to find ESPHome devices for UDP integration. This is only required for
people using ESPHome devices with the custom UDP component (not released yet!).

## Installation

### Step 1: Download files

#### Option 1: Via HACS

Make sure you have HACS installed.
If you don't, follow the steps [here](https://hacs.xyz/docs/setup/prerequisites) to install it.

Choose Integrations under HACS. Click the three '.'s in the top right corner and select custom repositories.
Paste the repository url `https://github.com/hass-emulated-hue/core-integration` and select `Integration`.
Click add. Select the `+ Explore & Download Repositories` button at the bottom right of the page and search
`Hass Emulated Hue` and select `Download this repository with HACS`.


#### Option 2: Manual
Clone this repository or download the source code as a zip file and add/merge the `custom_components/` folder with its contents in your configuration directory.


### Step 2: Restart HA
In order for the newly added integration to be loaded, HA needs to be restarted.

### Step 3: Add integration to HA
In HA, go to Configuration > Integrations.
In the bottom right corner, click on the big button with a '+'.

If the component is properly installed, you should be able to find the 'Hass Emulated Hue' in the list. You might need to clear you browser cache for the integration to show up.

***

[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg
[releases-shield]: https://img.shields.io/github/v/release/hass-emulated-hue/core-integration.svg
[releases]: https://github.com/hass-emulated-hue/core-integration/releases
