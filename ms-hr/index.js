const { server } = require("@the-medicsoft/webapi-framework");

// register routes
require('./routes/routeRegiser')(server);

module.exports = server;