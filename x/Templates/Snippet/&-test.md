
<%-*
const momentObj = moment(tp.file.title);
const firstDayOfMonth = momentObj.clone().startOf("month");
const firstDayOfWeek = firstDayOfMonth.clone().startOf("week");
const offset = firstDayOfMonth.diff(firstDayOfWeek, "days");
const weekOfMonth = Math.ceil((momentObj.date() + offset) / 7);
-%>
<% weekOfMonth %>


