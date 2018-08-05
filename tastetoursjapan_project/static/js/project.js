/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');

// section taken from material design google color tool via code pen
var buttons = document.querySelectorAll('.mdc-button, .mdc-fab');
for (var i = 0, button; button = buttons[i]; i++) {
  mdc.ripple.MDCRipple.attachTo(button);
}

var nodes = document.querySelectorAll('.mdc-icon-toggle');
for (var i = 0, node; node = nodes[i]; i++) {
  mdc.iconToggle.MDCIconToggle.attachTo(node);
}

var checkboxes = document.querySelectorAll('.mdc-checkbox');
for (var i = 0, checkbox; checkbox = checkboxes[i]; i++) {
  new mdc.checkbox.MDCCheckbox(checkbox);
}

var radios = document.querySelectorAll('.mdc-radio');
for (var i = 0, radio; radio = radios[i]; i++) {
  new mdc.radio.MDCRadio(radio);
}

var interactiveListItems = document.querySelectorAll('.mdc-list-item');
for (var i = 0, li; li = interactiveListItems[i]; i++) {
  mdc.ripple.MDCRipple.attachTo(li);
  // Prevent link clicks from jumping demo to the top of the page
  li.addEventListener('click', function(evt) {
    evt.preventDefault();
  });
}

// ed.on('init', function (ed) {
//     ed.target.editorCommands.execCommand("fontName", false, "Roboto");
// });
// datepicker
// Data Picker Initialization
// not used in prototype - commented out
// $('.datepicker').pickadate();
// // Strings and translations
// monthsFull: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
// monthsShort: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
// weekdaysFull: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
// weekdaysShort: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
// showMonthsShort: undefined,
// showWeekdaysFull: undefined,
//
// // Buttons
// today: 'Today',
// clear: 'Clear',
// close: 'Close',
//
// // Accessibility labels
// labelMonthNext: 'Next month',
// labelMonthPrev: 'Previous month',
// labelMonthSelect: 'Select a month',
// labelYearSelect: 'Select a year',
//
// // Formats
// format: 'd mmmm, yyyy',
// formatSubmit: undefined,
// hiddenPrefix: undefined,
// hiddenSuffix: '_submit',
// hiddenName: undefined,
//
// // Editable input
// editable: undefined,
//
// // Dropdown selectors
// selectYears: undefined,
// selectMonths: undefined,
//
// // First day of the week
// firstDay: undefined,
//
// // Date limits
// min: undefined,
// max: undefined,
//
// // Disable dates
// disable: undefined,
//
// // Root picker container
// container: undefined,
//
// // Hidden input container
// containerHidden: undefined,
//
// // Close on a user action
// closeOnSelect: true,
// closeOnClear: true,
//
// // Events
// onStart: undefined,
// onRender: undefined,
// onOpen: undefined,
// onClose: undefined,
// onSet: undefined,
// onStop: undefined,
//
// // Classes
// klass: {
//
//   // The element states
//   input: 'picker__input',
//   active: 'picker__input--active',
//
//   // The root picker and states *
//   picker: 'picker',
//   opened: 'picker--opened',
//   focused: 'picker--focused',
//
//   // The picker holder
//   holder: 'picker__holder',
//
//   // The picker frame, wrapper, and box
//   frame: 'picker__frame',
//   wrap: 'picker__wrap',
//   box: 'picker__box',
//
//   // The picker header
//   header: 'picker__header',
//
//   // Month navigation
//   navPrev: 'picker__nav--prev',
//   navNext: 'picker__nav--next',
//   navDisabled: 'picker__nav--disabled',
//
//   // Month & year labels
//   month: 'picker__month',
//   year: 'picker__year',
//
//   // Month & year dropdowns
//   selectMonth: 'picker__select--month',
//   selectYear: 'picker__select--year',
//
//   // Table of dates
//   table: 'picker__table',
//
//   // Weekday labels
//   weekdays: 'picker__weekday',
//
//   // Day states
//   day: 'picker__day',
//   disabled: 'picker__day--disabled',
//   selected: 'picker__day--selected',
//   highlighted: 'picker__day--highlighted',
//   now: 'picker__day--today',
//   infocus: 'picker__day--infocus',
//   outfocus: 'picker__day--outfocus',
//
//   // The picker footer
//   footer: 'picker__footer',
//
//   // Today, clear, & close buttons
//   buttonClear: 'picker__button--clear',
//   buttonClose: 'picker__button--close',
//   buttonToday: 'picker__button--today'
// }

// CHERRY BLOSSOM FALLING animation
