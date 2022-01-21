"""Hass Emulated Hue Component."""
from __future__ import annotations

from homeassistant import config_entries
from homeassistant.components.http import HomeAssistantView
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Enable the ESPHome IP API."""
    hass.http.register_view(ConfigEntryEsphomeView)
    return True


class ConfigEntryEsphomeView(HomeAssistantView):
    """View to get ESPHome IPs."""

    url = "/api/config/esphome/entries"
    name = "api:config:esphome:entries"

    async def get(self, request):
        """List available config entries."""
        hass = request.app["hass"]

        return self.json(
            [
                entry_json(entry)
                for entry in hass.config_entries.async_entries()
                if entry.domain == "esphome"
            ]
        )


@callback
def entry_json(entry: config_entries.ConfigEntry) -> dict:
    """Return JSON value of a config entry."""
    return {
        "entry_id": entry.entry_id,
        "host": entry.data.get("host"),
    }
