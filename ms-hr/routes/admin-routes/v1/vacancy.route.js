const { VacancyController } = require("../../../src/controllers");

module.exports = (fastify, option, done) => {
  const vacancies = new VacancyController();

  fastify.get("/vacancies", vacancies.getVacancies);

  done();
};
