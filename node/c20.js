#!/usr/bin/env node

var _ = require('lodash');
var iconMap = require('./maps/icons.map.json');
var currencyMap = require('./maps/currency.map.json');
var getData = require('./lib/get-data');

// enter number of tokens you have here
var num_c20_tokens = 1000;

/**
 * Calls different API's and prints out data
 * @returns {Promise.<void>}
 */
async function c20(){
    await getData.all();

    var nav = _.get(getData, 'data.c20.nav_per_token');

    console.log(`${nav} | templateImage=${iconMap['c20']}`);

}

c20()