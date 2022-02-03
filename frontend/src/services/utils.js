import moment from 'moment-timezone';

function formatDate(date) {
  const dateForConversion = moment.utc(date)
  return dateForConversion.tz('America/Sao_Paulo').format("DD/MM/YYYY HH:mm")
}

function getYear(date) {
  const dateForConversion = moment.utc(date)
  return dateForConversion.tz('America/Sao_Paulo').format("YYYY")
}

function getMonth(date) {
  const dateForConversion = moment.utc(date)
  return dateForConversion.tz('America/Sao_Paulo').format("MM")
}

export { formatDate, getYear, getMonth }