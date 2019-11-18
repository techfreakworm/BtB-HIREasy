const { Schema } = require("mongoose");

exports.VacancySchema = new Schema({
  skills: [String]
});
