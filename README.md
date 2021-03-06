[Alfred 2][alfred] Workflow for unit conversion
===============================================

<p align="center">
<img alt="Screenshot" src="http://dl.dropbox.com/s/gmep3v3hc5tvn57/jc-units_screenshot.png" />
</p>

<p align="center">
  <a href="http://dl.dropbox.com/s/kxzv83fkpw7caow/jc-units.alfredworkflow"><img src="http://dl.dropbox.com/s/m823ene4il9cnac/dl_button.png" alt="Download"></a>
</p>

This is a really simple workflow that just calls the Google calculator's unit
converter (http://www.google.com/ig/calculator) with your input. There are two
modes of operation: simple and query (described below).

The calculator is called as you type, so you might see a bit of weirdness while
you're inputing stuff. Just let it settle for a second when you're done
typing.

Actioning the result will copy the value (just the number) to the clipboard.
That's it!

### Simple

The simple mode is...simple.

    u {value} {in units} {out units}

You can include a space after the `u` keyword, but it's not required. Units can
generally be abbreviated or not, as long as the input is unambiguous.  You can
also throw an single word ("in", "to", "->", whatever) between the _in_ and
_out_ units for fun if you like. Some example commands:

* `u 5k to miles`
* `u 5k in miles`
* `u5k mi`

### Query

The query mode is more freeform.

    uq {input} {> out units}

The `> out units` bit is optional; if you don't specify, Google picks something
reasonable. This mode of operation lets you do math as well as simple
conversion, so you can do things like:

    1cm + 1in - 1mm > in

or

    1cm * 1mm > in^2

Installation
------------

To install, just download the [prepackaged workflow][pkg].  Double-click on the
downloaded file, or drag it into the Alfred Workflows window, and Alfred should
install it.

Requirements
------------

* Python 2.7 (standard in Lion and Mountain Lion)
* My [jcalfred][jcalfred] python library (included in the workflow download)

[pkg]: http://dl.dropbox.com/s/kxzv83fkpw7caow/jc-units.alfredworkflow
[jcalfred]: https://github.com/jason0x43/jcalfred
[alfred]: http://www.alfredapp.com
[icons]: http://www.weathericonsets.com
[wund]: http://www.weatherunderground.com
[fio]: http://forecast.io
