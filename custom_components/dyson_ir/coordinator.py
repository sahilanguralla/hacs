"""Data coordinator for Dyson IR devices."""
import logging
from datetime import timedelta
from typing import Any, Dict

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

_LOGGER = logging.getLogger(__name__)


class DysonIRCoordinator(DataUpdateCoordinator):
    """Data coordinator for Dyson IR devices."""

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:
        """Initialize coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name="Dyson IR",
            update_interval=timedelta(
                seconds=config_entry.options.get("update_interval", 300)
            ),
        )
        self.config_entry = config_entry
        self._device_state: Dict[str, Any] = {
            "power": False,
            "speed": 0,
            "oscillating": False,
            "heat": False,
        }

    async def _async_update_data(self) -> Dict[str, Any]:
        """Fetch data from device."""
        try:
            # Coordinator maintains local state since IR is fire-and-forget
            return self._device_state
        except Exception as err:
            raise UpdateFailed(f"Error updating Dyson IR: {err}") from err

    def set_device_state(self, state: Dict[str, Any]) -> None:
        """Update internal device state."""
        self._device_state.update(state)
        self.async_set_updated_data(self._device_state)
