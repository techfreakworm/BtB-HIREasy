const { BaseController } = require("@the-medicsoft/webapi-framework");

const { VacancyModel } = require("../models");

const vacancy = new VacancyModel();

class VacancyController extends BaseController {
  constructor() {
    super();
  }

  async getVacancies(req, res) {
    try {
      const response = await vacancy.getVacancies();

      super.sendResponse({ req, res, response });
    } catch (err) {
      super.sendErrorResponse({ req, res, errResponse: err });
    }
  }
}

module.exports = { VacancyController };
