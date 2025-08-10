import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import cover
from esphome.const import (
    CONF_ADDRESS, 
    CONF_ID, 
    CONF_UPDATE_INTERVAL, 
    CONF_USE_ADDRESS,
)

bus_t4_ns = cg.esphome_ns.namespace('bus_t4')
Nice = bus_t4_ns.class_('NiceBusT4', cover.Cover, cg.Component)

CONFIG_SCHEMA = (
    cover.cover_schema(Nice)
    .extend(
        {
            cv.GenerateID(): cv.declare_id(Nice),
            cv.Optional(CONF_ADDRESS): cv.hex_uint16_t,
            cv.Optional(CONF_USE_ADDRESS): cv.hex_uint16_t,
            #cv.Optional(CONF_UPDATE_INTERVAL): cv.positive_time_period_milliseconds,
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)

async def to_code(config):
    var = await cover.new_cover(config)
    await cg.register_component(var, config)
    await cover.register_cover(var, config)

    if CONF_ADDRESS in config:
        address = await cg.get_variable(config[CONF_ADDRESS])
        cg.add(var.set_to_address(address))
        
    if CONF_USE_ADDRESS in config:
        use_address = await cg.get_variable(config[CONF_USE_ADDRESS])
        cg.add(var.set_from_address(use_address))

 #   if CONF_UPDATE_INTERVAL in config:
 #       update_interval = config[CONF_UPDATE_INTERVAL]
 #       cg.add(var.set_update_interval(update_interval))
