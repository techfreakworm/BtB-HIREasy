const { BaseModel } = require("@the-medicsoft/webapi-framework");
const { model } = require("mongoose");

const { VacancySchema } = require("../schemas");

class VacancyModel extends BaseModel {
  constructor() {
    super(model("Vacancy", VacancySchema));
  }

  async getVacancies() {
    const vacancies = await super.read();

    if (vacancies) {
      return super.success({ total: vacancies.length, data: vacancies, message: '' });
    } else {
      super.notFound();
    }
  }
}

module.exports = { VacancyModel };
