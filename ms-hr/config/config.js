const BaseConfig = require("@the-medicsoft/webapi-framework/config").config;

class Config extends BaseConfig {
  constructor() {
    super();
    this.BASE_API_ROUTE = process.env.BASE_API_ROUTE || "/api";
    this.BASE_ADMIN_ROUTE = process.env.BASE_ADMIN_ROUTE || "/api";
  }
}

module.exports = new Config();
