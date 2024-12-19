Okay, let's break down this Bokeh changelog step-by-step. I will follow your instructions meticulously to provide comprehensive yet simple explanations for each change.

---

### Bokeh Version 2.2.3

---

<change_breakdown>
- **Change quoted:** "#10488 [component: bokehjs] In python3, rectangle does not appear when x axis is type datetime"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts listed:** Affects users using datetime objects on the x-axis with rectangle glyphs in Python 3.
- **Backward compatibility considered:** No backward compatibility issues; this is a fix.
- **Simple explanations brainstormed:** Rectangles weren't showing up on plots in Python 3 when the x-axis was a date or time. This was fixed.
- **Code examples outlined:**
    - Show a plot with datetime x-axis and rectangles not displaying before the fix.
    - Show the same plot after the fix, with rectangles displaying correctly.
- **One-sentence summary written:** Fixed an issue where rectangles wouldn't appear on plots with a datetime x-axis in Python 3.
</change_breakdown>

<change_number>1</change_number>
<change_description>
This change addresses a bug specific to Python 3 environments where rectangle glyphs were not rendering when the x-axis was configured to display datetime values.
</change_description>

<code_example>
```python
# Before fix (rectangles might not show)
from bokeh.plotting import figure, show
from datetime import datetime

p = figure(x_axis_type="datetime")
p.rect(x=[datetime(2023, 1, 1), datetime(2023, 1, 15)], y=[1, 2], width=1, height=1)
show(p)

# After fix (rectangles should show correctly)
from bokeh.plotting import figure, show
from datetime import datetime

p = figure(x_axis_type="datetime")
p.rect(x=[datetime(2023, 1, 1), datetime(2023, 1, 15)], y=[1, 2], width=1, height=1)
show(p)
```
</code_example>

<simple_explanation>
Imagine you're making a chart in Bokeh where the bottom axis (x-axis) represents dates. You want to add rectangles to your chart, but they don't show up if you're using Python 3. This update fixes that problem, so your rectangles will now appear correctly on the chart, even with dates on the x-axis.
</simple_explanation>

---

### Bokeh Version 2.2.2

---

<change_breakdown>
- **Change quoted:** "#10453 [component: server] [BUG] KeyError when display certain glyphs on the server"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts listed:**  Impacts users trying to display certain glyphs on the Bokeh server, causing a `KeyError`.
- **Backward compatibility considered:** No backward compatibility issues, this is a fix for a server-side error.
- **Simple explanations brainstormed:** Some shapes weren't showing up on the Bokeh server, throwing an error. This was fixed.
- **Code examples outlined:** N/A - hard to reproduce without specific glyph details and server setup, but generally demonstrate using the Bokeh server to display a glyph.
- **One-sentence summary written:** Fixed a bug where displaying certain glyphs on the Bokeh server would result in a `KeyError`.
</change_breakdown>

<change_number>2</change_number>
<change_description>
This fix resolves a server-side issue where certain glyphs would cause a `KeyError` when attempted to be displayed using the Bokeh server. The specific glyphs causing the error were not mentioned in the changelog.
</change_description>

<code_example>
```python
# General example of using Bokeh server (affected glyphs not specified)
# bokeh serve --show myapp.py 
# Where myapp.py contains:
from bokeh.plotting import figure
from bokeh.io import curdoc

p = figure()
# Assuming 'circle' was one of the affected glyphs (not confirmed)
p.circle([1, 2, 3], [4, 5, 6])
curdoc().add_root(p)
```
</code_example>

<simple_explanation>
Think of the Bokeh server as a way to show your charts to others online. Before this fix, if you tried to show certain shapes (glyphs) on your chart using the server, it would crash and give you an error. This update fixes that, so those shapes should now show up correctly when using the Bokeh server.
</simple_explanation>
<change_breakdown>
- **Change quoted:** "#10521 [component: bokehjs] Selectively update data when CDSView changes"
- **Change type:** Bug fix (likely performance improvement)
- **Change categorized:** Patch
- **Impacts listed:** Improves performance when using `CDSView` to filter data.
- **Backward compatibility considered:** No backward compatibility issues, this is an optimization.
- **Simple explanations brainstormed:** Using filters with `CDSView` to show parts of your data became more efficient. Only the necessary data is updated.
- **Code examples outlined:**
    - Show a plot with a `CDSView` and changing the filter.
    - Demonstrate that updates are more efficient.
- **One-sentence summary written:** Improved how Bokeh updates data when using `CDSView` to filter, resulting in better performance.
</change_breakdown>

<change_number>3</change_number>
<change_description>
This update optimizes the way Bokeh handles data updates when using a `CDSView`. `CDSView` allows you to filter data in a `ColumnDataSource`. This change ensures that when the filter in a `CDSView` is modified, only the relevant parts of the data are updated, rather than updating everything.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, IndexFilter
from bokeh.layouts import column
from bokeh.models.widgets import Button

source = ColumnDataSource(data=dict(x=[1, 2, 3, 4, 5], y=[2, 5, 8, 2, 7]))
view = CDSView(source=source, filters=[IndexFilter([0, 2, 4])])

p = figure(x_range=(0, 6), y_range=(0, 10))
p.circle(x='x', y='y', size=20, source=source, view=view)

button = Button(label="Change Filter")
button.on_click(lambda: view.filters.pop() if view.filters else view.filters.append(IndexFilter([1,3])))

show(column(p, button))
```
</code_example>

<simple_explanation>
Imagine you have a large dataset, but you only want to show some parts of it on your chart using a filter. Before, when you changed the filter, Bokeh would update the entire chart, even the parts you weren't looking at. Now, it's smarter and only updates the parts that actually changed because of the filter, making your chart faster and smoother.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#10451 [component: bokehjs] Update bokehjs' dependencies"
- **Change type:** Task
- **Change categorized:** Patch
- **Impacts listed:** Updates dependencies of the JavaScript library (bokehjs). Could bring in bug fixes, performance improvements, or new features from updated libraries.
- **Backward compatibility considered:** Generally, dependency updates should be backward compatible, but there's a slight risk of unexpected behavior if a dependency introduces breaking changes.
- **Simple explanations brainstormed:** Bokeh's JavaScript part (bokehjs) uses other libraries to work. These were updated to their latest versions, potentially bringing improvements.
- **Code examples outlined:** N/A - this is an internal change, not directly visible in user code.
- **One-sentence summary written:** Updated the external libraries used by bokehjs, potentially improving performance, stability, or features.
</change_breakdown>

<change_number>4</change_number>
<change_description>
This change is primarily internal. It involves updating the dependencies that Bokeh's JavaScript component (bokehjs) relies on. These dependencies are other JavaScript libraries that Bokeh uses to function correctly. Updating them might bring in bug fixes, performance improvements, or new features from those libraries.
</change_description>

<code_example>
N/A - This is an internal change and doesn't directly affect user-facing code.
</code_example>

<simple_explanation>
Bokeh's JavaScript part (bokehjs) relies on other pieces of JavaScript code (libraries) to do its job. This update is like upgrading those other pieces to their newer versions. It's like getting new, improved tools for building something – it might make the building process faster, the result stronger, or give you new options for what you can build.
</simple_explanation>

---

### Bokeh Version 2.2.1

---

<change_breakdown>
- **Change quoted:** "#10426 [component: bokehjs] INLINE_LEGACY does not work (CDN.legacy = True does work)"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts listed:** Affects users trying to use the `INLINE_LEGACY` resource mode.
- **Backward compatibility considered:** Fixes a bug with a legacy mode, no backward compatibility issues expected.
- **Simple explanations brainstormed:**  A way to include BokehJS (for older browsers) was broken but is now fixed.
- **Code examples outlined:** Demonstrate using `INLINE_LEGACY` resource mode.
- **One-sentence summary written:** Fixed an issue where the `INLINE_LEGACY` resource mode for loading BokehJS was not working.
</change_breakdown>

<change_number>5</change_number>
<change_description>
This change addresses a bug where the `INLINE_LEGACY` mode for loading BokehJS resources was not functioning correctly. This mode is used to include BokehJS resources directly within the HTML output, specifically targeting older browsers that might not support newer methods. The `CDN.legacy = True` mode, which serves BokehJS from a Content Delivery Network specifically for legacy browsers, was working correctly, but `INLINE_LEGACY` was not.
</change_description>

<code_example>
```python
# Using INLINE_LEGACY resource mode (now fixed)
from bokeh.resources import INLINE_LEGACY
from bokeh.embed import components
from bokeh.plotting import figure

p = figure()
p.line([1, 2, 3], [4, 5, 6])

script, div = components(p, resources=INLINE_LEGACY)

# Now you can embed 'script' and 'div' in your HTML.
```
</code_example>

<simple_explanation>
Bokeh needs a JavaScript part (BokehJS) to display charts in your web browser. `INLINE_LEGACY` is an older way to include this JavaScript part directly in your web page's code, especially for very old browsers. This method was broken, but now it's fixed. So if you need to support really old browsers, you can now use this method again.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#10431 [component: server] [BUG] pull_session not working in Win10 without this import statement: 'from bokeh.server.server import Server'"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts listed:** Affects users using `pull_session` on Windows 10. They needed an explicit import that is no longer required.
- **Backward compatibility considered:** Fixes a bug, no backward compatibility issues expected.
- **Simple explanations brainstormed:** Using `pull_session` on Windows 10 required an extra line of code (import). This is now fixed.
- **Code examples outlined:** Show code using `pull_session` without the extra import on Windows 10.
- **One-sentence summary written:** Fixed a bug where using `pull_session` on Windows 10 required an unnecessary import statement.
</change_breakdown>

<change_number>6</change_number>
<change_description>
This change fixes a bug specific to Windows 10 users when working with the Bokeh server and using the `pull_session` function. Previously, an explicit import statement `from bokeh.server.server import Server` was required to make `pull_session` work correctly on Windows 10. This import is no longer necessary after the fix.
</change_description>

<code_example>
```python
# Before fix (required extra import on Windows 10)
# from bokeh.server.server import Server  # No longer needed on Windows 10
from bokeh.client import pull_session
from bokeh.plotting import figure

# Now this works on Windows 10 without the extra import
with pull_session(url="http://localhost:5006/myapp") as session:
    # ... use the session ...
    pass
```
</code_example>

<simple_explanation>
Imagine you're connecting to a Bokeh server to display a chart. On Windows 10, you used to need an extra line of code (an "import") to make this connection work. This update removes that need. Now you can connect to the server on Windows 10 without that extra line, making your code a bit cleaner.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#10434 Bokeh not embedding plot in Django app sea_surface example [BUG]"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts listed:** Fixes an issue with embedding Bokeh plots in Django applications, specifically the `sea_surface` example.
- **Backward compatibility considered:** No backward compatibility issues, this is a fix.
- **Simple explanations brainstormed:**  Bokeh plots weren't showing up in a specific Django example. This is fixed now.
- **Code examples outlined:** N/A - Difficult to demonstrate without a complete Django project. Refer to the `sea_surface` example in the Bokeh repository.
- **One-sentence summary written:** Fixed a problem where Bokeh plots were not correctly embedded in a specific Django example application.
</change_breakdown>

<change_number>7</change_number>
<change_description>
This change specifically addresses an issue with embedding Bokeh plots into Django applications. The bug was demonstrated in the `sea_surface` example provided in the Bokeh repository. It likely involved an incompatibility or error in the way Bokeh was integrated into that particular Django project.
</change_description>

<code_example>
N/A - This bug is specific to a Django application example, and a minimal code example is difficult to construct without a full Django project setup. Refer to the `sea_surface` example in the Bokeh repository for details on how Bokeh is integrated with Django.
</code_example>

<simple_explanation>
Django is a popular framework for building websites. Bokeh can be used with Django to show interactive charts on those websites. There was a problem with a specific example (called `sea_surface`) that showed how to use Bokeh with Django - the charts weren't showing up. This update fixes that example, so now the charts display correctly in that Django application.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#10435 [BUG] Regression causing multiple js_on_event subscribers to be ignored"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts listed:** Affects users using multiple `js_on_event` callbacks. Only the first one would work; now they all work.
- **Backward compatibility considered:** Fixes a regression, should restore previous behavior.
- **Simple explanations brainstormed:**  If you had multiple JavaScript callbacks for an event, only the first one would run. Now they all run as expected.
- **Code examples outlined:** Show a plot with multiple `js_on_event` callbacks, demonstrating that all of them are now triggered.
- **One-sentence summary written:** Fixed a bug where only the first `js_on_event` callback would be executed, now all registered callbacks are triggered.
</change_breakdown>

<change_number>8</change_number>
<change_description>
This change fixes a regression (a bug introduced in a newer version that breaks something that used to work) related to using multiple JavaScript callbacks with the `js_on_event` method. `js_on_event` allows you to trigger JavaScript code when specific events occur on Bokeh objects. Previously, if you registered multiple callbacks for the same event, only the first one would be executed. This fix ensures that all registered callbacks are now triggered when the event occurs.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import CustomJS, Div
from bokeh.layouts import column

p = figure()
p.line([1, 2, 3], [4, 5, 6])

div = Div(text="Event Count: 0")

callback1 = CustomJS(args=dict(div=div), code="""
    div.text = "Event Count: 1";
    console.log('Callback 1 triggered');
""")

callback2 = CustomJS(args=dict(div=div), code="""
    div.text = "Event Count: 2";
    console.log('Callback 2 triggered');
""")

p.js_on_event('tap', callback1, callback2)

show(column(p, div))
```
</code_example>

<simple_explanation>
Let's say you want to do multiple things in your web browser whenever you click on a chart (a "tap" event). You can use `js_on_event` to tell Bokeh what to do when that event happens. Before, if you told Bokeh to do multiple things, it would only do the first one. This update fixes that, so now if you tell Bokeh to do several things when you click, it will do all of them, in order.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#10443 [BUG] incorrect Plot._check_bad_extra_range_name"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts listed:** Affects internal logic for checking extra range names. Likely no direct user impact, but fixes a potential source of errors.
- **Backward compatibility considered:** Fixes an internal bug, no backward compatibility issues expected.
- **Simple explanations brainstormed:** There was a mistake in the code that checks for extra range names. It's fixed now, preventing potential issues.
- **Code examples outlined:** N/A - Internal change, not directly visible in user code.
- **One-sentence summary written:** Fixed an internal error in how Bokeh checks for extra range names on plots.
</change_breakdown>

<change_number>9</change_number>
<change_description>
This change fixes an internal bug in the `Plot` class's `_check_bad_extra_range_name` method. This method is responsible for validating the names of extra ranges added to a plot. The exact nature of the bug is not detailed, but it likely involved an incorrect check or validation that could potentially lead to errors or unexpected behavior under certain circumstances.
</change_description>

<code_example>
N/A - This is an internal change related to how Bokeh handles extra ranges. It doesn't directly affect user-facing code, and a simple code example isn't applicable.
</code_example>

<simple_explanation>
Think of this as fixing a typo in the instruction manual that Bokeh uses internally. This typo could have potentially caused problems later on, but now that it's fixed, things should run more smoothly behind the scenes. It doesn't change how you use Bokeh, but it makes it more reliable.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#10448 [component: bokehjs] DataTable DateFormatter does not handle NaT"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts listed:** Affects `DataTable` with `DateFormatter` when dealing with "NaT" (Not a Time) values. These will now be displayed correctly.
- **Backward compatibility considered:** Fixes a bug, no backward compatibility issues expected.
- **Simple explanations brainstormed:** "NaT" values in `DataTable` dates were not displayed properly. This is now fixed.
- **Code examples outlined:** Show a `DataTable` with a column using `DateFormatter` and including "NaT" values.
- **One-sentence summary written:** Fixed an issue where "NaT" (Not a Time) values were not displayed correctly in `DataTable` columns using `DateFormatter`.
</change_breakdown>

<change_number>10</change_number>
<change_description>
This change fixes a bug in how `DataTable` handles "NaT" (Not a Time) values when using a `DateFormatter` to format date columns. "NaT" represents a missing or undefined datetime value. Previously, these values were not displayed correctly in the table; this fix ensures they are now handled and displayed appropriately (e.g., as an empty cell or a specific placeholder string).
</change_description>

<code_example>
```python
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn
from bokeh.io import show
import pandas as pd

data = {'dates': [pd.Timestamp('2023-01-10'), pd.NaT, pd.Timestamp('2023-01-12')]}
source = ColumnDataSource(data)

columns = [
    TableColumn(field="dates", title="Dates", formatter=DateFormatter()),
]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

show(data_table)
```
</code_example>

<simple_explanation>
Imagine you have a table (using `DataTable`) showing dates. Sometimes, you might have missing dates, represented by "NaT" (Not a Time). Before, these missing dates would show up weirdly in the table. This update fixes that, so now missing dates are displayed in a more understandable way, like an empty cell or a special placeholder.
</simple_explanation>

---

### Bokeh Version 2.2

---

<change_breakdown>
- **Change quoted:** "#5589 Some WebGL not working on Safari"
- **Change type:** Bug fix
- **Change categorized:** Minor
- **Impacts listed:** Fixes WebGL rendering issues in Safari. Users on Safari will have a better experience with WebGL-enabled plots.
- **Backward compatibility considered:**  No backward compatibility issues, this is a browser-specific fix.
- **Simple explanations brainstormed:** WebGL (for faster, smoother graphics) wasn't working correctly in Safari for some plots. This is fixed now.
- **Code examples outlined:** N/A - Difficult to demonstrate without knowing the specifics of what WebGL features were broken. Any WebGL-enabled plot should now work better in Safari.
- **One-sentence summary written:** Fixed issues with using WebGL for rendering plots in the Safari web browser.
</change_breakdown>

<change_number>11</change_number>
<change_description>
This change addresses issues with rendering plots using WebGL in the Safari web browser. WebGL is a technology that allows for hardware-accelerated rendering of graphics in the browser, often resulting in improved performance and smoother visuals. The specific details of what WebGL features were not working correctly in Safari are not mentioned, but this fix implies that various WebGL-enabled plots should now render more reliably and potentially with better performance in Safari.
</change_description>

<code_example>
N/A - This bug fix is related to specific WebGL rendering issues in Safari. A generic code example demonstrating WebGL usage might not fully illustrate the bug or its resolution. It's assumed that any plot using `output_backend="webgl"` should now render better in Safari.

```python
# Example of enabling WebGL rendering
from bokeh.plotting import figure, show

p = figure(output_backend="webgl")
p.circle([1, 2, 3], [4, 5, 6])
show(p)
```
</code_example>

<simple_explanation>
WebGL is like a turbocharger for your charts, making them faster and smoother. However, this turbocharger wasn't working perfectly in the Safari browser for some types of charts. This update fixes those problems, so now if you're using Safari, your WebGL-powered charts should look and perform better.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#6775 [component: bokehjs] SVG backend not correctly coloring glyphs in legends"
- **Change type:** Bug fix
- **Change categorized:** Minor
- **Impacts listed:** Affects SVG export where glyphs in legends were not colored correctly.
- **Backward compatibility considered:** No backward compatibility issues, this is a fix for SVG export.
- **Simple explanations brainstormed:** When exporting plots as SVG, the colors of shapes in the legend were wrong. This was fixed.
- **Code examples outlined:** Show a plot with a legend, export it as SVG, and show that the legend colors are now correct.
- **One-sentence summary written:** Fixed incorrect coloring of glyphs in legends when exporting plots to SVG format.
</change_breakdown>

<change_number>12</change_number>
<change_description>
This change addresses a bug in the SVG (Scalable Vector Graphics) export functionality of Bokeh. Specifically, it fixes an issue where glyphs (shapes representing data points) were not rendered with the correct colors in the legend when a plot was exported to SVG format.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show, output_file
from bokeh.io import export_svgs

p = figure()
p.circle([1, 2, 3], [4, 5, 6], color="red", legend_label="Red Circles")
p.line([1, 2, 3], [6, 2, 4], color="blue", legend_label="Blue Line")
p.legend.location = "top_left"

# This line is for making sure the output is SVG, it may not be needed with export_svg
# output_file("plot.html", mode="inline") 

p.output_backend = "svg"

export_svgs(p, filename="plot.svg")
show(p)
```
</code_example>

<simple_explanation>
SVG is a way to save your chart as an image that can be zoomed in without losing quality. Before this fix, if you saved your chart as an SVG, the colors of the shapes in the legend (the box that explains what each shape represents) might have been wrong. This update fixes that, so the legend colors in your saved SVG image will now be correct.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#7707 [component: bokehjs] Linking the ranges of plots will break the LODEnd event"
- **Change type:** Bug fix
- **Change categorized:** Minor
- **Impacts listed:** Affects users who link ranges of plots and use the `LODEnd` event.
- **Backward compatibility considered:** Fixes a bug, no backward compatibility issues.
- **Simple explanations brainstormed:** Linking ranges and using `LODEnd` (for actions after zoom/pan) didn't work together. This was fixed.
- **Code examples outlined:** Show two plots with linked ranges and demonstrate that the `LODEnd` event now works correctly.
- **One-sentence summary written:** Fixed an issue where the `LODEnd` event wouldn't fire correctly when ranges of plots were linked.
</change_breakdown>

<change_number>13</change_number>
<change_description>
This change fixes a bug related to linking the ranges of multiple plots and using the `LODEnd` event. `LODEnd` is an event that's triggered after a level-of-detail change, which typically happens after zooming or panning a plot. When ranges of plots are linked, zooming or panning one plot affects the others. This bug caused the `LODEnd` event to not fire correctly in such scenarios.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import CustomJS, Div
from bokeh.layouts import row

x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 8, 5, 1]

p1 = figure(width=300, height=300)
p1.line(x, y1, line_width=2)

p2 = figure(width=300, height=300, x_range=p1.x_range, y_range=p1.y_range)
p2.circle(x, y2, size=10, color="red")

div = Div(text="LODEnd event not triggered yet")

callback = CustomJS(args=dict(div=div), code="""
    div.text = "LODEnd event triggered!";
    console.log('LODEnd event triggered');
""")

p1.js_on_event('lodend', callback)
p2.js_on_event('lodend', callback)

show(row(p1, p2, div))
```
</code_example>

<simple_explanation>
Imagine you have two charts that are linked together, so when you zoom in on one, the other zooms in too. You also want something to happen after you finish zooming (that's what the `LODEnd` event is for). Before this fix, this "after zooming" action wouldn't work reliably when the charts were linked. Now it works correctly, so your action will happen every time you finish zooming on either of the linked charts.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#8046 [component: bokehjs] Extra whitespace with SVG export"
- **Change type:** Bug fix
- **Change categorized:** Minor
- **Impacts listed:** Affects SVG export, removing extra whitespace around the plot.
- **Backward compatibility considered:** No backward compatibility issues, this is a visual fix for SVG export.
- **Simple explanations brainstormed:** SVG exports had unnecessary white space around the plot. This was removed.
- **Code examples outlined:** Show a plot exported as SVG, demonstrating that the extra whitespace is now gone.
- **One-sentence summary written:** Fixed excessive whitespace around plots when exported to SVG format.
</change_breakdown>

<change_number>14</change_number>
<change_description>
This change addresses a visual issue with exporting plots to SVG format. Previously, exported SVGs might have contained extra, unnecessary whitespace around the plot area, leading to a less-than-ideal appearance when the SVG was displayed or embedded. This fix removes that extra whitespace, resulting in a cleaner and more accurate representation of the plot in SVG form.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.io import export_svgs

p = figure(width=200, height=200)
p.circle([1, 2, 3], [4, 5, 6])

p.output_backend = "svg"
export_svgs(p, filename="plot_without_whitespace.svg")
show(p)
```
</code_example>

<simple_explanation>
When you save your chart as an SVG image, it's like taking a picture of it. Before this fix, these pictures had extra white borders around them that weren't needed. This update removes those unnecessary borders, so your saved SVG images will now look exactly like your chart without any extra white space.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#8446 [component: bokehjs] SVG not displaying scatter output"
- **Change type:** Bug fix
- **Change categorized:** Minor
- **Impacts listed:** Affects scatter plots in SVG export. They were not displaying; now they are.
- **Backward compatibility considered:** No backward compatibility issues, this is a fix for SVG export.
- **Simple explanations brainstormed:** Scatter plots weren't showing up in SVG exports. This was fixed.
- **Code examples outlined:** Show a scatter plot exported as SVG, demonstrating that the points are now visible.
- **One-sentence summary written:** Fixed an issue where scatter plots were not rendered in SVG exports.
</change_breakdown>

<change_number>15</change_number>
<change_description>
This change resolves a bug where scatter plots were not being rendered at all when exported to SVG format. Scatter plots are a fundamental plot type used to display data points as individual markers. This fix ensures that scatter plots are now correctly included in SVG exports, allowing users to accurately represent their data in this format.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.io import export_svgs

p = figure()
p.scatter([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=10)

p.output_backend = "svg"
export_svgs(p, filename="scatter_plot.svg")
show(p)
```
</code_example>

<simple_explanation>
Imagine you made a scatter plot (a chart with dots representing data points) and wanted to save it as an SVG image. Before this fix, saving it would be like taking a picture of an empty space – the dots wouldn't show up in the image at all! This update fixes that, so now your saved SVG image will correctly show all the dots from your scatter plot.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#8744 [component: bokehjs] Plots containing arrows fail to render correctly with svg output backend."
- **Change type:** Bug fix
- **Change categorized:** Minor
- **Impacts listed:** Fixes rendering of plots with arrows when using the SVG output backend.
- **Backward compatibility considered:** No backward compatibility issues, this is a fix for SVG output.
- **Simple explanations brainstormed:** Arrows in plots weren't rendering correctly in SVG exports. This is fixed.
- **Code examples outlined:** Show a plot with arrows, export it as SVG, and show that the arrows now render correctly.
- **One-sentence summary written:** Fixed incorrect rendering of arrows in plots when using the SVG output backend.
</change_breakdown>

<change_number>16</change_number>
<change_description>
This change addresses a bug in the rendering of plots containing arrows when using the SVG output backend. Arrows are often used in plots to annotate or highlight specific data points or directions. Previously, when a plot with arrows was exported to SVG, the arrows might have been rendered incorrectly, potentially with incorrect positioning, size, or shape. This fix ensures that arrows are now rendered accurately in SVG exports.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import Arrow, OpenHead, NormalHead, VeeHead
from bokeh.io import export_svgs

p = figure(width=400, height=400)

p.circle([1, 2, 3], [2, 5, 3], size=20, color="#F08080")

p.add_layout(Arrow(end=OpenHead(line_color="firebrick", line_width=4),
                   x_start=1, y_start=

Okay, I'm ready to explain the Bokeh-Visualization library changelog. I will follow your instructions to provide detailed breakdowns and simple explanations for each change. Let's dive in!

## Bokeh-Visualization Changelog Explained

### Version 3.3 (Released 2023-10-10)

#### Bug Fixes

<change_breakdown>
[ ] Change quoted: "#7671 [component: bokehjs] Tool tip remains while using a scroll tool"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users who use tooltips in conjunction with scroll tools.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: The tooltip should disappear when the user starts scrolling, but it doesn't. This is fixed now.
[ ] Code examples outlined: No specific code example needed, as this is a behavioral fix.
[ ] One-sentence summary written: Fixed an issue where tooltips would persist on the screen even when using a scroll tool.
</change_breakdown>

<change_number>1</change_number>
<change_description>
This change addresses a bug where tooltips would remain visible on the plot even after the user started using a scroll tool. This could lead to tooltips overlapping with other elements or obscuring the data being visualized.
</change_description>

<code_example>
```python
# Not applicable for this behavioral fix
```
</code_example>

<simple_explanation>
Imagine you have a magnifying glass (tooltip) showing extra information about a point on a map. When you start moving the map around (using the scroll tool), the magnifying glass should disappear, but it didn't. This update fixes that, so the magnifying glass now disappears as expected when you move the map.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#11273 [component: bokehjs] [BUG] hover tooltip is cut off when the tooltip is tall and hover near the top of the plot"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users with tall tooltips displayed near the top of the plot.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: If a tooltip is too tall and displayed near the top, it gets cut off. Now, it should be displayed fully.
[ ] Code examples outlined: No specific code example needed, as this is a visual/layout fix.
[ ] One-sentence summary written: Fixed an issue where tall hover tooltips could be cut off when displayed near the top edge of the plot.
</change_breakdown>

<change_number>2</change_number>
<change_description>
This fix resolves a visual bug where tall hover tooltips displayed near the top of the plot would be cut off, making it difficult to read the full tooltip content. The tooltip's position is now adjusted to ensure it is fully visible within the plot area.
</change_description>

<code_example>
```python
# Not applicable for this visual/layout fix
```
</code_example>

<simple_explanation>
Think of a sticky note (tooltip) that's too long. If you stick it near the top edge of a whiteboard (plot), part of the note might go off the edge and you can't read it all. This update makes sure the sticky note is moved down a bit so you can see the whole message, even if it's a long one.
</simple_explanation>
<change_breakdown>
[ ] Change quoted: "#13170 [component: server] [BUG] Static paths loaded always from localhost in Bokeh 3.1.1"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users serving Bokeh applications with static resources (e.g., images, CSS) where the resources are not being loaded correctly from the specified location in Bokeh version 3.1.1.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: Bokeh was always trying to load static files from "localhost" (your own computer) even if you told it to look elsewhere. This is fixed now.
[ ] Code examples outlined: This issue might manifest in configuration or deployment, rather than in typical user code.
[ ] One-sentence summary written: Fixed a bug where static resource paths were incorrectly resolved to localhost, preventing proper loading of external resources.
</change_breakdown>

<change_number>3</change_number>
<change_description>
This bug fix addresses an issue introduced in Bokeh 3.1.1 where static resource paths were incorrectly resolved to `localhost`. This meant that Bokeh applications could not properly load external resources like images or CSS files if they were served from a different location. This fix ensures that static paths are resolved correctly based on the server configuration.
</change_description>

<code_example>
```python
# This issue is related to server configuration and deployment rather than typical user code.
# Example of specifying static resource paths in a Bokeh server application might be relevant
# but depends on how the server is set up.
```
</code_example>

<simple_explanation>
Imagine your website needs a picture that's stored on a different server. Bokeh (version 3.1.1) was mistakenly always looking for this picture on your own computer instead of the correct server. This update fixes that, so Bokeh now looks in the right place for your website's pictures and other files.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13195 [component: bokehjs] [BUG] WebGL with dashed line is not working when click_policy is muted"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users using WebGL to render dashed lines where the click policy is set to "mute."
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: Dashed lines drawn with WebGL didn't appear correctly when click actions were muted. This is now fixed.
[ ] Code examples outlined: Example showing WebGL rendering with dashed lines and click_policy set to "mute."
[ ] One-sentence summary written: Fixed a bug where dashed lines rendered with WebGL were not displayed correctly when the click policy was set to "mute."
</change_breakdown>

<change_number>4</change_number>
<change_description>
This change fixes a specific bug related to using WebGL for rendering dashed lines. When the `click_policy` of a glyph was set to `"mute"`, dashed lines were not rendered correctly. This fix ensures that dashed lines are displayed properly in WebGL mode, even with a muted click policy.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import Circle

p = figure(webgl=True)
p.line([1, 2, 3], [1, 2, 3], line_dash="dashed")  # Dashed line
circle = Circle(x=1, y=1, size=20, click_policy="mute") # Muted click policy
p.add_glyph(circle)

show(p)

```
</code_example>

<simple_explanation>
Imagine you're drawing a dashed line on a digital whiteboard using a special fast-drawing mode (WebGL). You also have a setting that says, "Don't do anything when I click on things" (click_policy="mute"). Before, this combination made your dashed line invisible. This update fixes it so your dashed line shows up correctly, even with the "no click actions" setting.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13196 Setting readonly properties in model constructors shouldn't be allowed"
[ ] Change type identified: Bug fix (more accurately, an enhancement to enforce constraints)
[ ] Change categorized: Patch
[ ] Impacts listed: Affects developers directly setting read-only properties during model initialization. These attempts will now likely raise errors.
[ ] Backward compatibility considered: May break code that incorrectly relied on setting read-only properties in constructors.
[ ] Simple explanations brainstormed: Some model properties are meant to be read-only. Before, you could try to set them when creating the model, but it wouldn't work as expected. Now, Bokeh stops you from doing that in the first place.
[ ] Code examples outlined: Example showing an attempt to set a read-only property in a constructor, which would previously have been silently ignored but will now raise an error.
[ ] One-sentence summary written: Enhanced Bokeh to prevent setting read-only properties during model construction, which was previously allowed but ineffective.
</change_breakdown>

<change_number>5</change_number>
<change_description>
This change strengthens the enforcement of read-only properties in Bokeh models. Previously, it was possible to attempt to set a read-only property during the initialization of a model, but this would be silently ignored. Now, such attempts will raise an error, making it clearer that these properties cannot be modified directly by the user.
</change_description>

<code_example>
```python
from bokeh.models import Range1d

# Assume 'start' is a read-only property calculated internally.
# In previous versions, the following line might have been silently ignored:
# r = Range1d(start=0, end=10)

# Now, it would likely raise an error, indicating that 'start' cannot be set directly.
# Example demonstrating the intended way (if any) to influence read-only properties
# would need to be based on the specific model and property.
```
</code_example>

<simple_explanation>
Imagine a toy with some parts that are fixed and can't be changed (read-only properties). Before, you could try to put them in a different place when building the toy, but it wouldn't actually change anything. Now, the toy instructions clearly tell you that you can't change those parts when building, preventing confusion.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13257 [BUG] FileNotFoundError when setting icon for BoxSelectTool"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users trying to set a custom icon for the `BoxSelectTool` using an external image file.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: Trying to use a custom image as an icon for the Box Select Tool would result in an error saying the file couldn't be found, even if it existed. This is fixed now.
[ ] Code examples outlined: Example showing how to set a custom icon for `BoxSelectTool` using a valid file path.
[ ] One-sentence summary written: Fixed a bug that prevented setting a custom icon for the `BoxSelectTool` from an external file, causing a `FileNotFoundError`.
</change_breakdown>

<change_number>6</change_number>
<change_description>
This bug fix addresses an issue where setting a custom icon for the `BoxSelectTool` using an external image file would result in a `FileNotFoundError`, even if the file existed and the path was correct. This fix ensures that the icon file is correctly located and loaded.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import BoxSelectTool

p = figure(tools="")
box_select = BoxSelectTool(icon="path/to/your/icon.png")  # Replace with your icon file path
p.add_tools(box_select)

p.line([1, 2, 3], [1, 2, 3])
show(p)
```
</code_example>

<simple_explanation>
Imagine you want to change the picture on a button (BoxSelectTool) to your own custom picture. Before, even if you had the picture file in the right place, Bokeh would say it couldn't find the picture. This update fixes that, so now you can successfully use your own picture for the button.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13284 [component: bokehjs] Reset WebGL changed flags on data glyph not visual glyphs"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users who rely on resetting WebGL-rendered plots and expect visual glyph properties (e.g., line style, color) to be reset to their default values.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: When resetting a plot using WebGL, some visual settings weren't being reset properly. This is fixed now.
[ ] Code examples outlined: No specific code example needed, as this is an internal fix related to the reset behavior of WebGL.
[ ] One-sentence summary written: Fixed a bug where resetting a WebGL-rendered plot did not correctly reset the visual properties of glyphs to their defaults.
</change_breakdown>

<change_number>7</change_number>
<change_description>
This change fixes a bug in how WebGL-rendered plots were reset. Previously, resetting a plot using WebGL would not correctly reset the visual properties of glyphs (like color or line style) back to their default values. This fix ensures that the reset operation now properly resets both the data and the visual aspects of the glyphs.
</change_description>

<code_example>
```python
# Not applicable, as this is an internal fix related to the reset behavior of WebGL.
```
</code_example>

<simple_explanation>
Imagine you have a drawing on an Etch-a-Sketch (WebGL plot). You change the color and thickness of the lines. When you shake the Etch-a-Sketch to reset it (reset the plot), the drawing disappears, but the color and thickness settings didn't go back to the original ones. This update fixes that, so shaking the Etch-a-Sketch now resets everything, including the color and thickness, back to how it was at the beginning.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13311 [component: tests] Bokeh build failing"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects developers building Bokeh from source. The build process was failing.
[ ] Backward compatibility considered: No backward compatibility issues (affects the build process, not runtime).
[ ] Simple explanations brainstormed: The process of building Bokeh from its source code was broken. This is fixed now.
[ ] Code examples outlined: Not applicable; this is a build process issue.
[ ] One-sentence summary written: Fixed an issue that caused the Bokeh build process to fail.
</change_breakdown>

<change_number>8</change_number>
<change_description>
This change addresses an issue that prevented Bokeh from being successfully built from its source code. This would primarily affect developers who are contributing to Bokeh or need to build a custom version of the library.
</change_description>

<code_example>
```python
# Not applicable; this is a build process issue.
```
</code_example>

<simple_explanation>
Imagine you have a set of instructions (source code) to build a LEGO castle (Bokeh). Before, some instructions were wrong, so you couldn't build the castle. This update fixes the instructions, so now you can build the castle successfully.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13315 [component: bokehjs] [BUG] RangeTool allows target plot to pan beyond explicit range bounds"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users who use `RangeTool` to control the visible range of a plot and have set explicit bounds on the target plot's range.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: The `RangeTool` was letting you pan the main plot outside the limits you set. Now it keeps the plot within the defined bounds.
[ ] Code examples outlined: Example showing a `RangeTool` applied to a plot with explicit range bounds, demonstrating that panning is now restricted.
[ ] One-sentence summary written: Fixed a bug where the `RangeTool` could allow panning a target plot beyond its explicitly set range bounds.
</change_breakdown>

<change_number>9</change_number>
<change_description>
This fix addresses a bug with the `RangeTool` where it was possible to pan the target plot beyond the explicitly defined range bounds. This could lead to unexpected behavior or display issues. The fix ensures that the `RangeTool` respects the specified range limits of the target plot.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import RangeTool, Range1d
from bokeh.layouts import column

# Main plot with explicit range bounds
x = [1, 2, 3, 4, 5]
y = [2, 5, 8, 2, 7]
p = figure(x_range=(2, 4), y_range=(0, 10))  # Explicit bounds
p.line(x, y)

# RangeTool controlling the main plot's x_range
range_tool = RangeTool(x_range=p.x_range)
range_tool_plot = figure(height=100, width=400,
                        y_range=p.y_range,
                        toolbar_location=None,
                        x_axis_type=None)
range_tool_plot.line(x, y)
range_tool_plot.add_tools(range_tool)

show(column(p, range_tool_plot))
```
</code_example>

<simple_explanation>
Imagine you have a window (plot) showing a part of a long scroll (data). You set limits on how far you can move the scroll left or right. The `RangeTool` is like a smaller window that lets you choose which part of the scroll the big window shows. Before, the small window could let you move the big window beyond the limits you set. This update fixes that, so the big window now stays within the limits, even when using the small window.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13323 [component: bokehjs] Layout is broken when using `RangeTool` and other weird behavior"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users who use `RangeTool` in their layouts. The layout could become broken or behave unexpectedly.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: Using `RangeTool` could mess up the arrangement of elements in the layout. This is fixed now.
[ ] Code examples outlined: No specific code example needed, as this is a general layout fix related to `RangeTool`.
[ ] One-sentence summary written: Fixed layout issues and unexpected behaviors that could occur when using the `RangeTool`.
</change_breakdown>

<change_number>10</change_number>
<change_description>
This change addresses various layout issues and unexpected behaviors that could occur when using the `RangeTool`. These issues could manifest as elements overlapping, being positioned incorrectly, or the layout otherwise not rendering as intended. This fix ensures that `RangeTool` interacts correctly with the layout system.
</change_description>

<code_example>
```python
# Not applicable, as this is a general layout fix related to `RangeTool`.
```
</code_example>

<simple_explanation>
Imagine you're arranging furniture (layout) in a room, and you have a special tool (RangeTool) that lets you zoom in on a part of the room. Before, using this tool could make the furniture overlap or move to the wrong places. This update fixes that, so the furniture stays in the right place even when you use the special zoom tool.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13347 [component: bokehjs] Long tooltip can trigger viewport scrollbars"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users with long tooltips that extend beyond the visible area of the plot. This could cause the entire page's scrollbars to appear.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: Very long tooltips could cause scrollbars to appear on the whole page, even if the plot itself didn't need them. Now, long tooltips are handled without affecting the page's scrollbars.
[ ] Code examples outlined: No specific code example needed, as this is a visual/layout fix related to tooltips.
[ ] One-sentence summary written: Fixed an issue where long tooltips could unintentionally trigger the appearance of the browser's viewport scrollbars.
</change_breakdown>

<change_number>11</change_number>
<change_description>
This change addresses a visual bug where lengthy tooltips could unintentionally trigger the appearance of the browser's viewport scrollbars. This could occur even if the plot itself did not require scrollbars, leading to a less-than-ideal user experience. This fix ensures that long tooltips are displayed correctly without affecting the page layout.
</change_description>

<code_example>
```python
# Not applicable, as this is a visual/layout fix related to tooltips.
```
</code_example>

<simple_explanation>
Imagine you have a small window (plot) and a very long sticky note (tooltip). Before, if the sticky note was too long to fit in the window, it would make the whole wall (page) get scrollbars, even if the wall itself didn't need them. This update fixes that, so now the long sticky note doesn't cause unnecessary scrollbars on the wall.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13369 [BUG] gridplot got multiple values for keyword argument 'logo'"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users who use the `gridplot` function and try to customize the `logo` property.
[ ] Backward compatibility considered: May break code that incorrectly passed the `logo` argument multiple times to `gridplot`.
[ ] Simple explanations brainstormed: `gridplot` was not handling the `logo` setting correctly if you provided it more than once. Now it works as expected.
[ ] Code examples outlined: Example showing the correct way to use the `logo` argument with `gridplot`.
[ ] One-sentence summary written: Fixed a bug where the `gridplot` function would raise an error if the `logo` argument was provided multiple times.
</change_breakdown>

<change_number>12</change_number>
<change_description>
This change fixes a bug in the `gridplot` function where providing the `logo` keyword argument multiple times would result in an error. This was due to `gridplot` not correctly handling duplicate keyword arguments. The fix ensures that `logo` is handled correctly, even if specified multiple times (although only the last specified value will likely be used).
</change_description>

<code_example>
```python
from bokeh.plotting import figure, gridplot, show

p1 = figure()
p1.circle([1, 2], [3, 4])
p2 = figure()
p2.line([1, 2], [3, 4])

# Correct usage of 'logo'
grid = gridplot([[p1, p2]], logo="grey") # Set logo to "grey" or None
show(grid)
```
</code_example>

<simple_explanation>
Imagine you're using a tool (gridplot) to arrange multiple pictures in a grid. You can add a small logo to the corner of the grid. Before, if you accidentally told the tool to use a logo more than once, it would get confused and stop working. This update fixes that, so the tool now handles the logo setting correctly, even if you repeat it by mistake.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13377 [component: bokehjs] [BUG] `value_throttled` being `Unset` prevents serialization of some widgets"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects users of widgets that have a `value_throttled` property. In some cases, these widgets might not have been serialized correctly, leading to issues in saving or displaying the plot.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: Some widgets have a setting called `value_throttled` that helps with performance. This setting wasn't being handled properly in some cases, which could cause problems when saving or showing the widget. This is fixed now.
[ ] Code examples outlined: No specific code example needed, as this is an internal fix related to widget serialization.
[ ] One-sentence summary written: Fixed a bug where the `value_throttled` property of some widgets, when in an unset state, could prevent proper serialization, leading to issues in saving or displaying plots.
</change_breakdown>

<change_number>13</change_number>
<change_description>
This change addresses a bug related to the serialization of widgets that have a `value_throttled` property. `value_throttled` is used to control how often a widget updates its value, improving performance by reducing the number of updates sent to the server. When `value_throttled` was in an unset state (`Unset`), it could prevent the widget from being serialized correctly, which could lead to problems when saving or displaying the plot. This fix ensures that widgets are serialized correctly regardless of the state of `value_throttled`.
</change_description>

<code_example>
```python
# Not applicable, as this is an internal fix related to widget serialization.
```
</code_example>

<simple_explanation>
Imagine you have a special kind of slider (widget) that has a setting to make it update smoothly (value_throttled). This setting was sometimes causing problems when you tried to save a picture of your work (serialization) or show it to others. This update fixes that, so the slider now works correctly even when you save or share your work.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13380 [component: tests] Examples tests are failing due to a missing dependency"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects developers running Bokeh's example tests. The tests were failing because a required library was missing.
[ ] Backward compatibility considered: No backward compatibility issues (affects tests, not runtime).
[ ] Simple explanations brainstormed: Some of the example tests for Bokeh weren't working because they needed an extra library that wasn't installed. This is fixed now.
[ ] Code examples outlined: Not applicable; this is a test dependency issue.
[ ] One-sentence summary written: Fixed an issue where some example tests were failing due to a missing dependency.
</change_breakdown>

<change_number>14</change_number>
<change_description>
This change ensures that the Bokeh example tests can be run successfully by adding a previously missing dependency. This would primarily affect developers who are working with the Bokeh codebase and need to run the tests.
</change_description>

<code_example>
```python
# Not applicable; this is a test dependency issue.
```
</code_example>

<simple_explanation>
Imagine you have a set of example exercises (tests) to learn how to use a new tool (Bokeh). Before, some exercises couldn't be done because you were missing a necessary tool (dependency). This update provides the missing tool, so now you can do all the exercises.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13400 [component: build] Release build fails with `FileNotFoundError`"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects the Bokeh release build process. The build was failing due to a missing file.
[ ] Backward compatibility considered: No backward compatibility issues (affects the build process, not runtime).
[ ] Simple explanations brainstormed: The process of creating a new official version of Bokeh was broken because a file was missing. This is fixed now.
[ ] Code examples outlined: Not applicable; this is a build process issue.
[ ] One-sentence summary written: Fixed a `FileNotFoundError` that was causing the Bokeh release build process to fail.
</change_breakdown>

<change_number>15</change_number>
<change_description>
This change addresses an issue that prevented the successful creation of a Bokeh release build due to a `FileNotFoundError`. This fix ensures that all necessary files are present during the release build process.
</change_description>

<code_example>
```python
# Not applicable; this is a build process issue.
```
</code_example>

<simple_explanation>
Imagine you're trying to package a gift (Bokeh release) to send to someone. You need to put all the items in a box (build). Before, you were missing one item, so you couldn't complete the package. This update makes sure all the items are there, so now you can successfully package the gift.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#13407 [component: tests] Tests and CI is broken due to urllib3 incompatibility"
[ ] Change type identified: Bug fix
[ ] Change categorized: Patch
[ ] Impacts listed: Affects running Bokeh's tests and continuous integration (CI) pipeline. They were failing due to an incompatibility with the `urllib3` library.
[ ] Backward compatibility considered: No backward compatibility issues (affects tests and CI, not runtime).
[ ] Simple explanations brainstormed: Bokeh's tests and automated checks weren't working because of a problem with a library called `urllib3`. This is fixed now.
[ ] Code examples outlined: Not applicable; this is a test/CI dependency issue.
[ ] One-sentence summary written: Fixed an incompatibility with the `urllib3` library that was causing Bokeh's tests and CI to fail.
</change_breakdown>

<change_number>16</change_number>
<change_description>
This change resolves an incompatibility issue with the `urllib3` library that was causing Bokeh's tests and continuous integration (CI) to fail. This ensures that the tests and CI pipeline can run successfully.
</change_description>

<code_example>
```python
# Not applicable; this is a test/CI dependency issue.
```
</code_example>

<simple_explanation>
Imagine you have a set of quality checks (tests and CI) that you run automatically whenever you make changes to a project (Bokeh). These checks were failing because of a problem with one of the tools (urllib3) they use. This update fixes the problem with the tool, so now the checks can run successfully again.
</simple_explanation>

#### Features

<change_breakdown>
[ ] Change quoted: "#2325 [component: bokehjs] Lasso select not working on patches"
[ ] Change type identified: Feature (enhancement/fix to existing feature)
[ ] Change categorized: Minor
[ ] Impacts listed: Affects users who want to use the Lasso Select tool with patch glyphs. Previously, this did not work correctly.
[ ] Backward compatibility considered: No backward compatibility issues.
[ ] Simple explanations brainstormed: The Lasso Select tool now works with patch glyphs, allowing users to select them.
[ ] Code examples outlined: Example showing the Lasso Select tool used with patch glyphs.
[ ] One-sentence summary written: Enhanced the Lasso Select tool to support selecting patch glyphs.
</change_breakdown>

<change_number>17</change_number>
<change_description>
This change enhances the Lasso Select tool to support selecting `Patches` glyphs. Previously, the Lasso Select tool did not function correctly with patches. This feature allows users to select multiple patch glyphs by drawing a freeform selection area around them.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import LassoSelectTool
from bokeh.models.sources import ColumnDataSource

p = figure(tools="lasso_select")
source = ColumnDataSource(data=dict(
    x=[[1, 2, 2, 1], [2, 3, 3, 2]],
    y=[[2, 2, 3, 3], [2, 2, 3, 3]],
))
p.patches('x', 'y', source=source, fill_alpha=0.5)
show(p)
```
</code_example>

<simple_explanation>
Imagine you have a map with different areas marked out (patches). You want to select multiple areas using a lasso tool, drawing a loop around them. Before, this didn't work. This update makes it possible to use the lasso tool to select these areas on the map.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#11571 [FEATURE] Make AutocompleteInput more usable by providing an option to match any part of the input items"
[ ] Change type identified: New feature
[ ] Change categorized: Minor
[ ] Impacts listed: Affects users of the `AutocompleteInput` widget. It now provides more flexible matching options.
[ ] Backward compatibility considered: No backward compatibility issues (adds a new option).
[ ] Simple explanations brainstormed: `AutocompleteInput` now has an option to suggest completions that match any part of the word, not just the beginning.
[ ] Code examples outlined: Example showing `AutocompleteInput` with the new matching option.
[ ] One-sentence summary written: Added a new option to `AutocompleteInput` to allow matching any part of the input items for suggestions.
</change_breakdown>

<change_number>18</change_number>
<change_description>
This change introduces a new feature to the `AutocompleteInput` widget, making it more flexible. A new option has been added that allows the autocomplete suggestions to match any part of the input items, not just the beginning. This makes the widget more user-friendly, especially when dealing with long or complex items.
</change_description>

<code_example>
```python
from bokeh.models.widgets import AutocompleteInput
from bokeh.io import show
from bokeh.layouts import column

# Before (default behavior - only matches from the beginning):
auto1 = AutocompleteInput(completions=["apple", "apricot", "banana", "avocado"], title="Match start:")

# New feature: match anywhere in the string
auto2 = AutocompleteInput(completions=["apple", "apricot", "banana", "avocado"], title="Match any:", case_sensitive=False, restrict=False)

show(column(auto1, auto2))
```
</code_example>

<simple_explanation>
Imagine you have a search box (AutocompleteInput) that helps you find words by suggesting completions as you type. Before, it would only suggest words that start with what you typed. Now, it has a new option to suggest words that contain what you typed anywhere in the word, making it easier to find what you're looking for.
</simple_explanation>

<change_breakdown>
[ ] Change quoted: "#11755 [FEATURE] Show scale in map"
[ ] Change type identified: New feature
[ ] Change categorized: Minor
[ ] Impacts listed: Affects users displaying maps. They can now show a scale indicator.
[ ] Backward compatibility considered: No backward compatibility issues (adds a new feature).
[ ] Simple explanations brainstormed: Maps can now display a scale, like "1 inch = 10 miles."
[ ] Code examples outlined: Example showing a map with a scale indicator.
[ ] One-sentence summary written: Added the ability to display a scale indicator on maps.
</change_breakdown>

<change_number>19</change_number>
<change_description>
This change introduces the ability to display a scale indicator on maps. This is a common and useful feature for map visualizations, providing context about the distances represented

Okay, let's break down this Bokeh changelog! I'll go through each entry, providing detailed explanations, code examples, and simple summaries for each change.

## Bokeh Changelog Breakdown and Explanations

### 2018-12-31    1.0.3:

<change_breakdown>
- Change quoted: "#7118 [component: bokehjs] Unable to update arrow"
- Change type identified: Bug fix
- Change categorized: Patch
- Impacts listed: Fixes issues with updating Arrow annotations dynamically.
- Backward compatibility considered: No backward compatibility issues expected.
- Simple explanations brainstormed: "Arrows couldn't be updated before, now they can."
- Code examples outlined: Show how to update an Arrow's properties after creation.
- One-sentence summary written: This bug fix allows for the dynamic updating of Arrow annotations in BokehJS.
</change_breakdown>

<change_number>1</change_number>
<change_description>
This change addresses a bug where Arrow annotations in Bokeh plots could not be updated after they were initially created. The fix ensures that properties of an Arrow, such as its start and end points, color, or line width, can be modified, and the changes will be reflected in the plot.
</change_description>

<code_example>
```python
from bokeh.models import Arrow, OpenHead, ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.io import curdoc

p = figure(width=400, height=400)
source = ColumnDataSource(data=dict(x_start=[1], y_start=[2], x_end=[2], y_end=[3]))
arrow = Arrow(end=OpenHead(line_color="firebrick", line_width=4),
              x_start='x_start', y_start='y_start', x_end='x_end', y_end='y_end', source=source)
p.add_layout(arrow)

def update():
    source.data = dict(x_start=[2], y_start=[3], x_end=[3], y_end=[4])

curdoc().add_root(p)
curdoc().add_periodic_callback(update, 1000)

# Run this with: bokeh serve --show myapp.py
```
</code_example>

<simple_explanation>
Imagine you drew an arrow on a chart, but then you wanted to change where it points or its color. Before this fix, Bokeh wouldn't let you update the arrow. Now, you can easily change the arrow's properties, and the chart will update accordingly. This makes plots with arrows more dynamic and interactive.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8401 [API: models] Incorrect image import from bokeh.models"
- Change type identified: Bug fix
- Change categorized: Patch
- Impacts listed: Fixes incorrect import statements that might have caused errors when using specific image models.
- Backward compatibility considered: No backward compatibility issues expected.
- Simple explanations brainstormed: "Some imports were wrong, leading to errors; now they are fixed."
- Code examples outlined: No specific code example needed, as it's an internal fix.
- One-sentence summary written: This bug fix corrects an internal issue with how images were imported within the Bokeh library.
</change_breakdown>

<change_number>2</change_number>
<change_description>
This change fixes an internal issue where certain image-related models in Bokeh were not being imported correctly. This could have potentially led to errors when trying to use these models in your code. The fix corrects the import paths, ensuring that the models are available as expected.
</change_description>

<code_example>
Not applicable for this internal fix.
</code_example>

<simple_explanation>
Think of it like a library having some books misfiled. You wouldn't be able to find them when you needed them. This fix is like putting those books back in the right place so that Bokeh can find and use them correctly. You don't need to change anything in your code; it just works better now.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8493 [component: bokehjs] Polydrawtool shows vertices even when not active"
- Change type identified: Bug fix
- Change categorized: Patch
- Impacts listed: Fixes the behavior of the PolyDrawTool, ensuring vertices are only visible when the tool is active.
- Backward compatibility considered: No backward compatibility issues expected.
- Simple explanations brainstormed: "The drawing tool showed dots even when not in use; now it doesn't."
- Code examples outlined: Demonstrates the correct behavior of the PolyDrawTool (active/inactive).
- One-sentence summary written: The PolyDrawTool now correctly hides vertices when the tool is not active, improving the visual experience.
</change_breakdown>

<change_number>3</change_number>
<change_description>
This bug fix addresses an issue with the `PolyDrawTool` where the vertices (the points that define the polygon) were visible even when the tool was not actively being used. This could be visually distracting or confusing. With this fix, the vertices are only shown when the `PolyDrawTool` is active, providing a cleaner and more intuitive user experience.
</change_description>

<code_example>
```python
# No specific code example is needed to demonstrate the fix.
# The behavior is corrected internally within the PolyDrawTool.
# When the tool is active, you'll see vertices; when inactive, you won't.
```
</code_example>

<simple_explanation>
Imagine using a drawing tool where the dots you connect to draw lines are always visible, even when you're not drawing. It would be messy, right? This fix makes sure those dots only appear when you're actively using the drawing tool, making the plot look cleaner when you're not drawing.
</simple_explanation>
<change_breakdown>
- Change quoted: "#2828 [component: bokehjs] [widgets] Multi-line textinput box?"
- Change type identified: New feature
- Change categorized: Minor
- Impacts listed: Introduces a multi-line text input widget.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "You can now have text input boxes that allow multiple lines of text."
- Code examples outlined: Show how to create and use a `TextAreaInput` widget.
- One-sentence summary written: This feature adds a `TextAreaInput` widget for multi-line text input in Bokeh applications.
</change_breakdown>

<change_number>4</change_number>
<change_description>
This change introduces a new widget called `TextAreaInput`, which allows users to input multiple lines of text. This is different from the existing `TextInput` widget, which is limited to a single line. The `TextAreaInput` widget is useful for collecting larger blocks of text from users, such as comments, descriptions, or other free-form input.
</change_description>

<code_example>
```python
from bokeh.models import TextAreaInput
from bokeh.io import curdoc
from bokeh.layouts import column

text_area = TextAreaInput(value="", title="Enter some text:", rows=6)

def callback(attr, old, new):
    print("New text area value:", new)

text_area.on_change("value", callback)

curdoc().add_root(column(text_area))
# Run with: bokeh serve --show myapp.py
```
</code_example>

<simple_explanation>
Think of the old text input like a single-line form field, good for a name or email. This new multi-line text input is like a bigger box where you can write a whole paragraph or more, like a comment box on a website. It allows users to enter and view longer text entries within your Bokeh application.
</simple_explanation>
<change_breakdown>
- Change quoted: "#7762 [component: bokehjs] Copy & paste from datatable"
- Change type identified: New feature
- Change categorized: Minor
- Impacts listed: Enables copy and paste functionality for the DataTable widget.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "You can now copy data from the DataTable and paste it elsewhere."
- Code examples outlined: No specific code example needed, as it's a built-in feature.
- One-sentence summary written: This feature adds the ability to copy and paste data to and from the DataTable widget.
</change_breakdown>

<change_number>5</change_number>
<change_description>
This feature enhances the `DataTable` widget by adding the capability to copy data from the table and paste it into other applications, such as spreadsheets or text editors. It also enables pasting data into the DataTable, making it easier to populate or edit the table's contents. This is a significant usability improvement for interacting with tabular data in Bokeh applications.
</change_description>

<code_example>
```python
# No specific code example is needed.
# The copy-paste functionality is built into the DataTable widget.
# Users can select cells, rows, or the entire table and use standard
# keyboard shortcuts (e.g., Ctrl+C, Ctrl+V) or context menu options
# to copy and paste data.
```
</code_example>

<simple_explanation>
Imagine you have a table of data in your Bokeh app, and you want to copy some of it into an Excel sheet. Before this feature, you couldn't. Now, you can simply select the data you want in the DataTable, copy it, and paste it wherever you need it. It's like copying and pasting from any other table you're used to.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8444 [component: bokehjs] Feature request: expose sort_columns in js datatable object"
- Change type identified: New feature
- Change categorized: Minor
- Impacts listed: Exposes the `sort_columns` property in the JavaScript DataTable object, allowing for programmatic sorting from JavaScript callbacks.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "You can now control how the DataTable is sorted from JavaScript code."
- Code examples outlined: Show how to access and modify `sort_columns` in a CustomJS callback.
- One-sentence summary written: This feature allows developers to programmatically control the sorting of a DataTable from JavaScript.
</change_breakdown>

<change_number>6</change_number>
<change_description>
This change exposes the `sort_columns` property of the `DataTable` widget in the JavaScript API. This allows developers to control the sorting of the table programmatically from JavaScript callbacks, enabling more dynamic and interactive table behavior. For example, you could trigger a re-sort of the table based on user interactions with other widgets or events.
</change_description>

<code_example>
```javascript
// In a CustomJS callback:

const table = data_table_widget; // Assuming you have a reference to your DataTable widget
const source = table.source;

// Sort by the 'value' column in ascending order
table.sort_columns = [{ field: 'value', sortAsc: true }];

// Trigger an update of the table view
source.change.emit();
```
</code_example>

<simple_explanation>
Imagine you have a button in your Bokeh app, and you want it to sort the data in your DataTable when clicked. Before this, you couldn't easily do that from JavaScript code. Now, you can access the table's sorting settings in JavaScript and change them, causing the table to re-sort itself based on your instructions.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8502 Support environment variable in addition to --allow-websocket-origin"
- Change type identified: New feature
- Change categorized: Minor
- Impacts listed: Adds support for an environment variable (`BOKEH_ALLOW_WS_ORIGIN`) to specify allowed websocket origins.
- Backward compatibility considered: No backward compatibility issues, as it adds an alternative way to configure the setting.
- Simple explanations brainstormed: "You can now set allowed origins for websockets using an environment variable, besides the command line."
- Code examples outlined: Show how to set the `BOKEH_ALLOW_WS_ORIGIN` environment variable.
- One-sentence summary written: This feature introduces an environment variable to configure allowed websocket origins, providing an alternative to the command-line option.
</change_breakdown>

<change_number>7</change_number>
<change_description>
This change adds support for an environment variable, `BOKEH_ALLOW_WS_ORIGIN`, as an alternative to the `--allow-websocket-origin` command-line argument for specifying the allowed origins for websocket connections to a Bokeh server. This is useful for configuring security settings, especially in containerized or automated deployment environments where setting environment variables is more convenient than passing command-line arguments.
</change_description>

<code_example>
```bash
# Set the environment variable before starting the Bokeh server:
export BOKEH_ALLOW_WS_ORIGIN=example.com:80,another.com:8080

# Or, on Windows:
set BOKEH_ALLOW_WS_ORIGIN=example.com:80,another.com:8080

# Then start the Bokeh server as usual:
bokeh serve myapp.py
```
</code_example>

<simple_explanation>
Imagine you're setting up a Bokeh server and need to tell it which websites are allowed to connect to it. Before, you could only do this by typing a special command when starting the server. Now, you can also set this up beforehand, like writing it down in a configuration file, using an environment variable. This makes it easier to manage security settings, especially in automated setups.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8372 Extended bad_column_name error"
- Change type identified: Task (Improvement)
- Change categorized: Minor
- Impacts listed: Improves the error message when an invalid column name is used.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "The error message for using a wrong column name is now more helpful."
- Code examples outlined: No specific code example needed.
- One-sentence summary written: This improvement provides a more informative error message when an invalid column name is used with a ColumnDataSource.
</change_breakdown>

<change_number>8</change_number>
<change_description>
This change improves the error message that is displayed when a user tries to access a column in a `ColumnDataSource` that does not exist. The new error message provides more context and guidance, making it easier to debug and correct the issue. This is a general improvement to the user experience, especially for those new to Bokeh.
</change_description>

<code_example>
```python
# No specific code example is needed.
# The improved error message will be displayed automatically when you try
# to access a non-existent column in a ColumnDataSource.
```
</code_example>

<simple_explanation>
Imagine you're looking for a specific book in a library, but you get the title wrong. A helpful librarian wouldn't just say, "Book not found." They'd say, "We don't have a book with that exact title. Did you mean [similar title]?" This change is like that helpful librarian. When you use a wrong column name in your code, Bokeh now gives you a better error message, helping you figure out what went wrong more easily.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8379 [component: examples] Export csv example more useful if you don't have to hard code headers in download.js"
- Change type identified: Task (Improvement)
- Change categorized: Minor
- Impacts listed: Improves the "export CSV" example by making it more flexible.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "The CSV export example now works better without needing to hardcode column names."
- Code examples outlined: No specific code example needed, as it refers to an example improvement.
- One-sentence summary written: This improvement modifies the "export CSV" example to dynamically determine column headers, removing the need for hardcoding.
</change_breakdown>

<change_number>9</change_number>
<change_description>
This change updates the "export CSV" example in the Bokeh examples directory. Previously, the example required hardcoding the column headers in the JavaScript code used for downloading the CSV file. This made the example less flexible and harder to adapt to different datasets. The updated example dynamically determines the column headers from the data source, making it more reusable and easier to understand.
</change_description>

<code_example>
```
# While no specific code change is shown here, the improvement
# would be in the download.js file of the "export CSV" example.
# Instead of hardcoding headers like:
# const headers = ["col1", "col2", "col3"];
# It would dynamically get them from the ColumnDataSource,
# perhaps like:
# const headers = Object.keys(source.data);
```
</code_example>

<simple_explanation>
Imagine you have an example showing how to export data to a CSV file, but it only works if your data has specific column names. This improvement is like making the example smarter, so it can figure out the column names automatically from your data. This way, you can use the example with any dataset without having to change the code that handles the export.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8383 [component: tests] Attempt to enable downstream tests for holoviews"
- Change type identified: Task
- Change categorized: Minor
- Impacts listed: Improves testing coverage by enabling downstream tests for HoloViews.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "Testing is improved by including tests for libraries that depend on Bokeh, like HoloViews."
- Code examples outlined: No specific code example needed.
- One-sentence summary written: This task focuses on improving the testing process by enabling downstream tests for libraries that depend on Bokeh, such as HoloViews.
</change_breakdown>

<change_number>10</change_number>
<change_description>
This change is related to the testing infrastructure of Bokeh. It enables downstream tests for HoloViews, which is a library that builds on top of Bokeh. Downstream tests are important for ensuring that changes in Bokeh do not break libraries that depend on it. By enabling these tests, the Bokeh development team can catch potential issues earlier and ensure better compatibility with the broader ecosystem.
</change_description>

<code_example>
Not applicable for this testing infrastructure change.
</code_example>

<simple_explanation>
Imagine you're updating a popular board game (Bokeh). You want to make sure that any expansions people have created for your game (like HoloViews) still work with the new version. Downstream tests are like checking these expansions to make sure they're still compatible. This change enables these checks, making sure that Bokeh continues to work well with other tools in the ecosystem.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8384 [component: bokehjs] Feature: add plot's root id to dom so to allow api access to the object"
- Change type identified: New feature
- Change categorized: Minor
- Impacts listed: Adds the plot's root ID to the DOM, making it easier to access the plot object from external JavaScript code.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "You can now find the plot object more easily from outside of Bokeh's JavaScript code."
- Code examples outlined: Show how to access the plot object using the root ID from the DOM.
- One-sentence summary written: This feature adds the plot's root ID to the DOM, enabling easier access to the plot object from external JavaScript code.
</change_breakdown>

<change_number>11</change_number>
<change_description>
This change adds the root ID of a Bokeh plot to the Document Object Model (DOM). The root ID is a unique identifier for the plot object. By adding it to the DOM, it becomes easier to access the plot object from external JavaScript code, such as browser extensions or other scripts that interact with the page. This can be useful for advanced customization or integration of Bokeh plots into larger web applications.
</change_description>

<code_example>
```html
<!-- Assuming a Bokeh plot is embedded in this div -->
<div id="my-bokeh-plot"></div>

<script>
  // After the plot is rendered, you can access it like this:
  const plotId = document.getElementById("my-bokeh-plot").dataset.rootId;
  const plotView = Bokeh.index[plotId];

  // Now you can interact with the plot object (plotView)
  // For example, you could change its properties or call its methods
</script>
```
</code_example>

<simple_explanation>
Imagine you have a Bokeh plot embedded in a webpage, and you want to control it using some JavaScript code that's not part of Bokeh. Before this change, it was a bit tricky to find the plot object from your code. Now, it's like the plot has a name tag (the root ID) attached to it in the webpage's structure (the DOM). Your external code can easily find the plot by looking for this name tag and then interact with it.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8472 Boilerplates for bokeh/models"
- Change type identified: Task
- Change categorized: Minor
- Impacts listed: Provides boilerplate code for creating new Bokeh models.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "There's now starter code available to help create new Bokeh models more easily."
- Code examples outlined: No specific code example needed, as it refers to the availability of boilerplate code.
- One-sentence summary written: This task introduces boilerplate code to simplify the creation of new custom Bokeh models.
</change_breakdown>

<change_number>12</change_number>
<change_description>
This change introduces boilerplate code for creating new Bokeh models. Bokeh models are the fundamental building blocks of Bokeh plots, representing everything from data sources and glyphs to widgets and layouts. Providing boilerplate code makes it easier for developers to extend Bokeh's functionality by creating their own custom models. This can be useful for creating specialized visualizations or widgets that are not available in the standard Bokeh library.
</change_description>

<code_example>
Not applicable, as this refers to the availability of boilerplate code within the Bokeh codebase.
</code_example>

<simple_explanation>
Imagine you want to create a new type of chart or widget that doesn't exist in Bokeh yet. Before this change, you'd have to start from scratch, which could be quite complicated. Now, it's like having a template or a starting point (boilerplate code) that you can use to build your new model. This makes it easier and faster to extend Bokeh with your own custom components.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8476 [component: bokehjs] [typescript] Upgrade to typescript 3.2"
- Change type identified: Task
- Change categorized: Minor
- Impacts listed: Updates the TypeScript version used in BokehJS to 3.2.
- Backward compatibility considered: No backward compatibility issues expected.
- Simple explanations brainstormed: "BokehJS now uses a newer version of TypeScript, which brings improvements and bug fixes."
- Code examples outlined: No specific code example needed.
- One-sentence summary written: This task upgrades the TypeScript version used in BokehJS to 3.2, bringing various improvements and bug fixes to the JavaScript codebase.
</change_breakdown>

<change_number>13</change_number>
<change_description>
This change updates the version of TypeScript used in the BokehJS codebase to 3.2. TypeScript is a superset of JavaScript that adds static typing, which can help catch errors during development and improve code maintainability. Upgrading to a newer version of TypeScript brings various improvements, such as new language features, performance enhancements, and bug fixes. This benefits the development of BokehJS but does not directly affect users of the Bokeh library.
</change_description>

<code_example>
Not applicable for this internal codebase update.
</code_example>

<simple_explanation>
Imagine you're using a tool to write code, and the tool gets an update with new features and bug fixes. This change is like that update for Bokeh's JavaScript codebase. It's now using a newer, better version of the tool (TypeScript), which helps the developers write better code and fix issues more easily. You don't need to change anything in your code; it's an internal improvement.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8481 [component: docs] Doc: remove extra "to execute" from embed"
- Change type identified: Task (Documentation)
- Change categorized: Minor
- Impacts listed: Corrects a minor error in the documentation.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "A small error in the documentation was fixed."
- Code examples outlined: No specific code example needed.
- One-sentence summary written: This task corrects a minor wording error in the documentation related to embedding Bokeh plots.
</change_breakdown>

<change_number>14</change_number>
<change_description>
This change is a simple correction to the Bokeh documentation. It removes the phrase "to execute" where it was not needed in the section about embedding Bokeh plots. This is a minor improvement to the clarity and accuracy of the documentation.
</change_description>

<code_example>
Not applicable for this documentation correction.
</code_example>

<simple_explanation>
It's like finding a small typo in a textbook. This change fixes that typo in the Bokeh documentation, making it a little bit clearer and more accurate.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8485 Update sampledata bucket url"
- Change type identified: Task
- Change categorized: Minor
- Impacts listed: Updates the URL for downloading sample data.
- Backward compatibility considered: No backward compatibility issues if users update their code to use the new URL.
- Simple explanations brainstormed: "The location where Bokeh's sample data is stored has changed."
- Code examples outlined: Show how to use the new URL for downloading sample data.
- One-sentence summary written: This task updates the URL for accessing Bokeh's sample datasets.
</change_breakdown>

<change_number>15</change_number>
<change_description>
This change updates the URL used for downloading Bokeh's sample datasets. The sample datasets are used in many of Bokeh's examples and tutorials. If you have code that relies on the old URL, you will need to update it to use the new URL. This change ensures that the sample data remains accessible and that the examples continue to work correctly.
</change_description>

<code_example>
```python
from bokeh.sampledata import download

# Previously, download() would fetch from the old URL
# Now, it uses the updated URL
download()
```
</code_example>

<simple_explanation>
Imagine Bokeh's sample datasets are like books in a library, and the library moved to a new address. This change updates the address (URL) so that you can still find and use those datasets. If you have code that uses the old address, you'll need to update it to the new one.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8491 [component: docs] Typo in range_tool example"
- Change type identified: Task (Documentation)
- Change categorized: Minor
- Impacts listed: Corrects a typo in the `range_tool` example.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "A typo in an example was fixed."
- Code examples outlined: No specific code example needed.
- One-sentence summary written: This task fixes a typo in the `range_tool` example in the documentation.
</change_breakdown>

<change_number>16</change_number>
<change_description>
This change corrects a typo in the `range_tool` example in the Bokeh documentation. The `range_tool` example demonstrates how to use the `RangeTool` to interactively select a range on a plot. Fixing the typo ensures that the example is accurate and easy to understand.
</change_description>

<code_example>
Not applicable for this documentation correction.
</code_example>

<simple_explanation>
It's like finding a typo in a recipe. This change fixes that typo in one of Bokeh's examples, making the instructions clearer and more accurate.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8495 [component: tests] Document licenses of included projects"
- Change type identified: Task
- Change categorized: Minor
- Impacts listed: Improves documentation by documenting the licenses of included projects.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "The licenses for external libraries used by Bokeh are now clearly documented."
- Code examples outlined: No specific code example needed.
- One-sentence summary written: This task adds documentation about the licenses of external projects included in Bokeh.
</change_breakdown>

<change_number>17</change_number>
<change_description>
This change adds documentation about the licenses of third-party projects that are included in Bokeh. This is important for transparency and legal compliance. By clearly documenting the licenses, users of Bokeh can be aware of the terms under which these external components are used.
</change_description>

<code_example>
Not applicable for this documentation update.
</code_example>

<simple_explanation>
Imagine you're using a piece of software that includes components from other developers. This change is like adding a clear statement of what the licenses are for those components, so everyone knows the terms of use. It's about being transparent and making sure everything is legally sound.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8506 Boilerplate for bokeh/plotting directory"
- Change type identified: Task
- Change categorized: Minor
- Impacts listed: Provides boilerplate code for the `bokeh/plotting` directory.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "There's now starter code for the `bokeh/plotting` part of the library."
- Code examples outlined: No specific code example needed.
- One-sentence summary written: This task introduces boilerplate code for the `bokeh/plotting` directory, simplifying development within this part of the library.
</change_breakdown>

<change_number>18</change_number>
<change_description>
Similar to change #12, this change introduces boilerplate code, but this time for the `bokeh/plotting` directory. The `bokeh/plotting` interface is a higher-level API for creating Bokeh plots. Providing boilerplate code makes it easier for developers to contribute to or extend the `bokeh/plotting` interface.
</change_description>

<code_example>
Not applicable, as this refers to the availability of boilerplate code within the Bokeh codebase.
</code_example>

<simple_explanation>
This is similar to change #12. Imagine you want to improve or add to the way Bokeh lets you create plots. This change provides a template or starting point (boilerplate code) specifically for that part of Bokeh (the `bokeh/plotting` directory). It's like giving you a head start when working on that specific area of the library.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8514 Boilerplate for protocol"
- Change type identified: Task
- Change categorized: Minor
- Impacts listed: Provides boilerplate code for the Bokeh protocol.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "There's now starter code for the part of Bokeh that handles communication between the server and the browser."
- Code examples outlined: No specific code example needed.
- One-sentence summary written: This task introduces boilerplate code for the Bokeh protocol, simplifying development related to Bokeh's communication mechanism.
</change_breakdown>

<change_number>19</change_number>
<change_description>
This change introduces boilerplate code for the Bokeh protocol. The Bokeh protocol defines how data and events are transmitted between the Bokeh server and the browser. Providing boilerplate code makes it easier for developers to work with or extend the protocol, for example, to optimize communication or add new message types.
</change_description>

<code_example>
Not applicable, as this refers to the availability of boilerplate code within the Bokeh codebase.
</code_example>

<simple_explanation>
Imagine you want to improve the way Bokeh sends information between the server and your browser. This change is like providing a template or starting point (boilerplate code) for that communication part of Bokeh (the protocol). It makes it easier to work on that area and potentially make communication more efficient or add new ways for the server and browser to talk to each other.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8517 Boilerplate for bokeh/server"
- Change type identified: Task
- Change categorized: Minor
- Impacts listed: Provides boilerplate code for the `bokeh/server` directory.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "There's now starter code for the part of Bokeh that deals with the server."
- Code examples outlined: No specific code example needed.
- One-sentence summary written: This task introduces boilerplate code for the `bokeh/server` directory, simplifying development related to the Bokeh server.
</change_breakdown>

<change_number>20</change_number>
<change_description>
This change introduces boilerplate code for the `bokeh/server` directory. This part of the Bokeh codebase deals with the server component that handles communication with clients and manages application state. Providing boilerplate code makes it easier for developers to contribute to or extend the Bokeh server, for example, to add new features or customize its behavior.
</change_description>

<code_example>
Not applicable, as this refers to the availability of boilerplate code within the Bokeh codebase.
</code_example>

<simple_explanation>
Similar to the previous boilerplate changes, this one provides a template or starting point (boilerplate code) for working on the server part of Bokeh. It's like giving developers a head start when they want to improve or customize how the Bokeh server works.
</simple_explanation>
<change_breakdown>
- Change quoted: "#8523 Property getter for model.id"
- Change type identified: Task (Improvement)
- Change categorized: Minor
- Impacts listed: Adds a property getter for `model.id`, making it easier to access the ID of a model.
- Backward compatibility considered: No backward compatibility issues.
- Simple explanations brainstormed: "You can now get the ID of a model more easily."
- Code examples outlined: Show how to access the ID using the new property getter.
- One-sentence summary written: This improvement adds a property getter for `model.id`, simplifying access to a model's unique identifier.
</change_breakdown>

<change_number>21</change_number>
<change_description>
This change adds a property getter for the `id` attribute of Bokeh models. Every Bokeh model has a unique ID that identifies it. The property getter makes it easier to access this ID. This is a minor convenience improvement for developers working with Bokeh models.
</change_description>

<code_example>
```python
from bokeh.models import Slider

slider = Slider(start=0, end=10, value=5, step=1, title="My Slider")

# Accessing the model's ID using the new property getter:
model_id = slider.id
print(model_id)
```
</code_example>

<simple_explanation>
Imagine every component in your Bokeh plot (like a slider or a button) has a unique ID number. This change is like making it easier to find out that ID number. You can now just ask for it directly (using `model.id`) instead of having to go through a

Let's break down this Bokeh changelog. Here's a detailed explanation of each change, designed to be accessible even to junior developers:

# Bokeh Changelog Explanation

## Version 2.4.2 (2021-11-22)

### Bug Fixes

<change_breakdown>
> "#11422 [component: bokehjs] [BUG] `DeserializationError` when trying to change a `DataTable`'s columns with `CustomJS`"

- **Change type:** Bug fix
- **Change categorized:** Patch (minor)
- **Impacts:** Affects users who modify `DataTable` columns dynamically using JavaScript callbacks (`CustomJS`).
- **Backward compatibility:** No issues, fixes a bug.
- **Simple explanations:**  There was a problem where changing the columns of a data table using JavaScript code would cause an error. This has been fixed.
- **Code examples:** Modifying `DataTable` columns with `CustomJS`.
- **One-sentence summary:** Fixed an error that occurred when updating `DataTable` columns using `CustomJS`.
</change_breakdown>

<change_number>1</change_number>
<change_description>
This bug fix addresses an issue where attempting to modify the columns of a `DataTable` widget using a `CustomJS` callback would result in a `DeserializationError`. This error likely occurred due to problems in how the changes made through JavaScript were being communicated back to the Python side of Bokeh.
</change_description>

<code_example>
```python
from bokeh.models import ColumnDataSource, DataTable, TableColumn, CustomJS
from bokeh.io import show
from bokeh.layouts import column

# Initial data and columns
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
source = ColumnDataSource(data)
columns = [
    TableColumn(field="col1", title="Column 1"),
    TableColumn(field="col2", title="Column 2"),
]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

# CustomJS to add a new column
callback = CustomJS(args=dict(source=source, columns=columns, table=data_table), code="""
    // Add a new column to the data
    source.data['col3'] = [7, 8, 9];

    // Create a new column definition
    const newColumn = {field: 'col3', title: 'Column 3'};

    // Add the new column to the existing columns array
    columns.push(newColumn);

    // Update the table's columns
    table.columns = columns;
    source.change.emit();
""")

# Add a button to trigger the callback
from bokeh.models import Button
button = Button(label="Add Column", button_type="success")
button.js_on_click(callback)

show(column(data_table, button))
```
</code_example>

<simple_explanation>
Imagine you have a table displayed on a webpage, and you want to add a new column to it using some JavaScript code. Before this fix, Bokeh would throw an error when you tried to do this. Now, you can add or modify columns in your table using JavaScript without any problems.
</simple_explanation>

<change_breakdown>
> "#11800 [BUG] DeserializationError when plotting graphs"

- **Change type:** Bug fix
- **Change categorized:** Patch (minor)
- **Impacts:** Affects users plotting graphs, especially those with complex interactions or updates.
- **Backward compatibility:** No issues, fixes a bug.
- **Simple explanations:** There was a problem causing errors when creating or updating graph plots. This is now fixed.
- **Code examples:** Plotting graphs using `bokeh.plotting` or `bokeh.models.GraphRenderer`.
- **One-sentence summary:** Fixed an error that appeared when plotting graphs, especially when making updates to them.
</change_breakdown>

<change_number>2</change_number>
<change_description>
This fix addresses a `DeserializationError` that could occur when working with graph plots. This type of error typically arises when there's a mismatch between the data being sent from the browser (JavaScript) to the Python backend, or vice-versa. It could have affected various graph plotting scenarios, especially those involving dynamic updates or interactions.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import GraphRenderer, Circle, StaticLayoutProvider
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc

# Basic graph setup (this part would have been more complex in a real failing scenario)
plot = figure(title="Graph Plot", x_range=(-2, 2), y_range=(-2, 2),
              tools="", toolbar_location=None)

graph = GraphRenderer()
graph.node_renderer.data_source.add([1, 2, 3], 'index')
graph.node_renderer.data_source.add(['a', 'b', 'c'], 'names')
graph.node_renderer.glyph = Circle(size=15, fill_color="blue")

graph.edge_renderer.data_source.data = dict(
    start=[1, 2],
    end=[2, 3])

# This layout would likely be more dynamic and cause issues in the failing cases
graph_layout = {1: (0, 0), 2: (1, 1), 3: (-1, -1)}
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
plot.renderers.append(graph)

# Example of a change that could have triggered the error before the fix
def update_graph():
    # Modify node positions or add/remove nodes/edges
    new_layout = {1: (0.5, 0.5), 2: (1.5, 1.5), 3: (-0.5, -0.5), 4: (0, -1)}
    graph.layout_provider.graph_layout = new_layout
    graph.node_renderer.data_source.add([4], 'index')
    graph.node_renderer.data_source.add(['d'], 'names')
    graph.edge_renderer.data_source.data = dict(
        start=[1, 2, 3, 1],
        end=[2, 3, 4, 4])

# Add the plot to the current document (could be served with 'bokeh serve')
curdoc().add_root(plot)
curdoc().add_periodic_callback(update_graph, 1000) # Update every second

show(plot)
```
</code_example>

<simple_explanation>
Sometimes, when you were creating or changing a graph visualization, Bokeh would show an error. This was especially true if you were adding or removing parts of the graph or moving things around. This fix makes sure that creating and changing graphs works smoothly without that error.
</simple_explanation>

<change_breakdown>
> "#11801 [component: bokehjs] [BUG] Log axis figures don't render if they're not visible at start"

- **Change type:** Bug fix
- **Change categorized:** Patch (minor)
- **Impacts:** Affects users using logarithmic axes that are initially hidden (e.g., in a tab or collapsed panel).
- **Backward compatibility:** No issues, fixes a bug.
- **Simple explanations:** Plots with log scales wouldn't show up if they were hidden initially. Now, they render correctly even if they start off hidden.
- **Code examples:** Creating plots with `y_axis_type="log"` or `x_axis_type="log"` inside layouts like `Tabs`.
- **One-sentence summary:** Fixed an issue where plots with log axes didn't render if they were initially hidden.
</change_breakdown>

<change_number>3</change_number>
<change_description>
This bug fix addresses a rendering problem specific to plots using logarithmic axes. If a plot with a log axis was initially hidden from view (for example, if it was inside a tab that wasn't active or within a collapsed panel), it would fail to render even when made visible later. This issue was likely related to how BokehJS (the JavaScript part of Bokeh) initializes and renders plots when they become visible.
</change_description>

<code_example>
```python
from bokeh.plotting import figure
from bokeh.models import Panel, Tabs
from bokeh.io import show
from bokeh.layouts import column

# Create a plot with a log axis
plot = figure(y_axis_type="log", title="Log Axis Plot", width=400, height=400)
plot.line([1, 2, 3, 4, 5], [1, 10, 100, 1000, 10000], line_width=2)

# Create a panel with the log plot (initially hidden)
tab1 = Panel(child=plot, title="Log Plot")

# Create another panel with a regular plot
plot2 = figure(title="Regular Plot", width=400, height=400)
plot2.circle([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], size=10)
tab2 = Panel(child=plot2, title="Regular Plot")

# Create tabs
tabs = Tabs(tabs=[tab1, tab2])

# Before the fix, the log plot might not render when its tab was selected
show(tabs)
```
</code_example>

<simple_explanation>
Imagine you have two charts: one normal and one that shows data in a special way called a "log scale", which is useful for showing a wide range of values. If you put these charts into tabs, where only one is visible at a time, the log scale chart might not have appeared when you switched to its tab. This fix ensures that the log scale chart appears correctly, even if it wasn't visible when the page first loaded.
</simple_explanation>

<change_breakdown>
> "#11807 [component: bokehjs] Work around issues with initialization-time change discovery"

- **Change type:** Bug fix
- **Change categorized:** Patch (minor)
- **Impacts:** Affects various Bokeh models during their initialization, improving overall stability.
- **Backward compatibility:** No issues, fixes a bug.
- **Simple explanations:**  Bokeh had some problems figuring out changes made to plots and widgets when they were first created. This update improves how Bokeh detects those initial changes.
- **Code examples:** This is an internal change; user-level code examples won't directly demonstrate it.
- **One-sentence summary:** Improved how Bokeh detects initial changes to models, making it more stable.
</change_breakdown>

<change_number>4</change_number>
<change_description>
This change is more of an internal improvement within BokehJS. It addresses issues related to how Bokeh detects and handles changes to model properties during the initialization phase. These issues might have manifested as various unexpected behaviors or inconsistencies in how plots or widgets were rendered or updated initially. By improving the change discovery mechanism, this fix enhances the overall stability and reliability of Bokeh.
</change_description>

<code_example>
This is an internal change in how Bokeh handles object initialization. There's no user-facing code example that would directly demonstrate this change.
</code_example>

<simple_explanation>
When you create a chart or a widget in Bokeh, you set some initial properties like its size, color, or data. Sometimes, Bokeh had trouble figuring out exactly what those initial settings were, which could lead to unexpected behavior. This fix helps Bokeh understand the initial settings better, so your charts and widgets work more consistently.
</simple_explanation>

<change_breakdown>
> "#11808 Don't unnecessarily update node/edge renderers in graphs"

- **Change type:** Bug fix (performance optimization)
- **Change categorized:** Patch (minor)
- **Impacts:** Improves performance when working with graph plots, especially large ones.
- **Backward compatibility:** No issues, it's an optimization.
- **Simple explanations:** Graph plots were being updated more often than necessary, which could slow things down. This change makes sure updates only happen when needed.
- **Code examples:** Working with `GraphRenderer` and updating its data source or layout.
- **One-sentence summary:** Optimized graph rendering to avoid unnecessary updates, improving performance.
</change_breakdown>

<change_number>5</change_number>
<change_description>
This change is a performance optimization for graph plots. In previous versions, Bokeh might have been updating the visual representation of nodes and edges in a graph more frequently than necessary. This could lead to slowdowns, especially when dealing with large or complex graphs. This fix ensures that the node and edge renderers are only updated when there are actual changes to the underlying data or layout, resulting in smoother and more efficient rendering.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show, from_networkx
from bokeh.models import GraphRenderer, StaticLayoutProvider
import networkx as nx

# Create a sample graph using NetworkX
G = nx.karate_club_graph()

# Create a Bokeh plot
plot = figure(title="Karate Club Graph", x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
              tools="", toolbar_location=None)

# Create a Bokeh graph from the NetworkX graph
graph = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

# Add the graph renderer to the plot
plot.renderers.append(graph)

# Example of an update that might have been unnecessarily expensive before
# Now it's optimized to only update if something actually changed
def update_graph_data():
    # In a real scenario, you might add/remove nodes or edges here
    # Or change node/edge properties that affect the visual representation
    pass  # No changes for this example

# Simulate periodic updates (e.g., in a Bokeh server app)
from bokeh.io import curdoc
curdoc().add_root(plot)
curdoc().add_periodic_callback(update_graph_data, 2000)  # Check for updates every 2 seconds
show(plot)
```
</code_example>

<simple_explanation>
If you have a graph visualization (like a network of friends or connections), Bokeh was sometimes redrawing the entire graph even when nothing had changed. This could make things slow, especially if the graph was very large. This update makes sure Bokeh only redraws the graph when something actually changes, like when you add a new connection or move things around, making it faster and smoother.
</simple_explanation>

### Tasks

<change_breakdown>
> "#11613 [component: docs] Cache-bust custom.css for docs"

- **Change type:** Task (documentation improvement)
- **Change categorized:** Patch (minor)
- **Impacts:** Improves the developer experience when contributing to Bokeh documentation.
- **Backward compatibility:** No issues.
- **Simple explanations:** Ensures that the latest version of the documentation's CSS file is always loaded, preventing issues with cached outdated styles.
- **Code examples:** N/A - this relates to documentation build process.
- **One-sentence summary:** Updated the documentation build process to ensure the latest CSS is always used.
</change_breakdown>

<change_number>6</change_number>
<change_description>
This change relates to the Bokeh documentation build process. It ensures that when the documentation is updated, the latest version of the `custom.css` file (which contains custom styles for the documentation) is always loaded by the browser. This is achieved through "cache-busting," which typically involves adding a version number or hash to the CSS file's URL, forcing the browser to download the new version instead of using a cached older version.
</change_description>

<code_example>
This change doesn't have a user-facing code example. It affects how the Bokeh documentation is built and served.
</code_example>

<simple_explanation>
When you visit a website, your browser often saves parts of it (like style sheets) so it can load faster next time. This is called "caching." Sometimes, if the website's style sheet changes, your browser might still use the old saved version, making the website look wrong. This update makes sure that when the Bokeh documentation is updated, your browser always gets the latest style sheet, so the documentation always looks as it should.
</simple_explanation>

<change_breakdown>
> "#11791 [component: docs] Update issue template to use new GH forms"

- **Change type:** Task (documentation/process improvement)
- **Change categorized:** Patch (minor)
- **Impacts:** Improves the process of reporting issues on GitHub.
- **Backward compatibility:** No issues.
- **Simple explanations:** The template used for creating new issues on Bokeh's GitHub repository has been updated to use GitHub's new forms, making it easier to report bugs and request features.
- **Code examples:** N/A - relates to GitHub issue reporting.
- **One-sentence summary:** Updated the GitHub issue template to use the new GitHub forms.
</change_breakdown>

<change_number>7</change_number>
<change_description>
This change updates the way issues are reported on Bokeh's GitHub repository. It replaces the old issue template with the new GitHub Forms feature. This makes it easier for users to report bugs or request new features by providing a more structured and user-friendly way to enter the necessary information.
</change_description>

<code_example>
This change doesn't have a user-facing code example. It affects the issue reporting process on GitHub.
</code_example>

<simple_explanation>
When you want to report a problem or suggest a new feature for Bokeh, you do it on GitHub. This change makes that process easier by using a new GitHub feature called "Forms." Instead of writing everything in a text box, you'll now have specific fields to fill in, which helps make sure you provide all the important information.
</simple_explanation>

<change_breakdown>
> "#11761 [component: docs] Clarify use of color in first steps guide"

- **Change type:** Task (documentation improvement)
- **Change categorized:** Patch (minor)
- **Impacts:** Improves the clarity of the introductory documentation.
- **Backward compatibility:** No issues.
- **Simple explanations:** The "first steps" guide has been updated to explain how to use colors in Bokeh plots more clearly.
- **Code examples:** Examples in the first steps guide related to setting colors of glyphs or other plot elements.
- **One-sentence summary:** Improved the explanation of color usage in the introductory documentation.
</change_breakdown>

<change_number>8</change_number>
<change_description>
This change improves the "first steps" guide in the Bokeh documentation by providing a clearer explanation of how to use colors in plots. This could involve clarifying the different ways colors can be specified (e.g., named colors, hex codes, RGB tuples), how to apply colors to different plot elements (e.g., lines, markers, fills), and any other relevant details about color usage in Bokeh.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show

# Create a plot
p = figure(width=400, height=400)

# Add a circle with a specific color (using a named color)
p.circle([1, 2, 3], [4, 5, 6], size=20, color="navy", alpha=0.5)

# Add a line with a specific color (using a hex code)
p.line([1, 2, 3], [6, 5, 4], line_width=2, color="#FF0000")

# Show the plot
show(p)
```
</code_example>

<simple_explanation>
If you're new to Bokeh, the "first steps" guide helps you get started. This update makes it easier to understand how to use colors in your charts. For example, it might explain how to make a line red, a circle blue, or how to use different shades of colors.
</simple_explanation>

<change_breakdown>
> "#11762 [component: docs] Replace slash with backslash for PS commands"

- **Change type:** Task (documentation fix)
- **Change categorized:** Patch (minor)
- **Impacts:** Corrects a minor error in the documentation related to PowerShell commands.
- **Backward compatibility:** No issues.
- **Simple explanations:** Fixed a typo in the documentation where forward slashes were used instead of backslashes in PowerShell commands.
- **Code examples:** N/A - documentation fix related to command syntax.
- **One-sentence summary:** Corrected the use of slashes in PowerShell commands in the documentation.
</change_breakdown>

<change_number>9</change_number>
<change_description>
This is a small correction to the documentation. In Windows PowerShell, backslashes (`\`) are typically used as path separators and in certain command syntax, whereas forward slashes (`/`) are more common in Unix-like systems. This change ensures that the documentation uses the correct backslash character for PowerShell commands, avoiding potential confusion or errors for users who are copying and pasting commands from the docs.
</change_description>

<code_example>
This change doesn't have a user-facing code example. It's a correction of command syntax in the documentation. Instead of something like `command /option`, it would now be `command \option` in relevant places.
</code_example>

<simple_explanation>
In Windows, when you're typing commands in PowerShell, you often use backslashes (`\`) instead of forward slashes (`/`). The Bokeh documentation had a typo where it used the wrong slash. This fix corrects that typo, so the commands in the documentation are now correct for PowerShell.
</simple_explanation>

<change_breakdown>
> "#11767 [component: bokehjs] Upgrade jquery-ui to resolve security concerns"

- **Change type:** Task (dependency update)
- **Change categorized:** Patch (minor)
- **Impacts:** Improves the security of BokehJS by updating a dependency.
- **Backward compatibility:** Should be no issues, but might require testing if custom extensions rely on jQuery UI.
- **Simple explanations:** The jQuery UI library, which Bokeh uses, has been updated to a newer version to address security vulnerabilities.
- **Code examples:** N/A - this is a dependency update, not a direct code change.
- **One-sentence summary:** Updated jQuery UI to a more secure version.
</change_breakdown>

<change_number>10</change_number>
<change_description>
This change updates the version of the jQuery UI library used by BokehJS. jQuery UI is a popular JavaScript library that provides various user interface interactions, widgets, and effects. The update was likely made to address security vulnerabilities that were discovered in older versions of jQuery UI. By upgrading to a newer, more secure version, Bokeh helps protect users from potential security risks.
</change_description>

<code_example>
This is a dependency update, not a direct code change. User-level Bokeh code won't be directly affected.
</code_example>

<simple_explanation>
Bokeh uses other software libraries to help it do its job. One of these libraries is called jQuery UI, which helps with things like interactive elements on a webpage. The old version of jQuery UI had some security problems, so this update replaces it with a newer, safer version. It's like upgrading the locks on your house to make them more secure.
</simple_explanation>

<change_breakdown>
> "#11781 [component: examples] fix transform jitter example"

- **Change type:** Task (example fix)
- **Change categorized:** Patch (minor)
- **Impacts:** Fixes a specific example demonstrating jitter transformations.
- **Backward compatibility:** No issues.
- **Simple explanations:** The example demonstrating the jitter transform was broken; this change fixes it.
- **Code examples:** The `transform_jitter.py` example in the Bokeh examples directory.
- **One-sentence summary:** Fixed the broken jitter transform example.
</change_breakdown>

<change_number>11</change_number>
<change_description>
This change fixes a specific example in the Bokeh examples collection. The example, likely named something like `transform_jitter.py`, demonstrates the use of the `Jitter` transform. This transform is used to add random noise or "jitter" to data points, which can be useful for visualizing overlapping data. The fix likely addresses issues that were preventing the example from running correctly or producing the expected output.
</change_description>

<code_example>
The specific code example would be the `transform_jitter.py` (or similarly named) file in the Bokeh examples. The fix would involve correcting the code within that example to make it function as intended. You'll need to look at the exact example code in the Bokeh repository to see the specific fix.
</code_example>

<simple_explanation>
Bokeh has example code to show you how to use different features. One of these examples, which shows how to spread out overlapping data points (called "jittering"), was broken. This fix makes that example work correctly again, so you can learn how to use jittering in your own charts.
</simple_explanation>

<change_breakdown>
> "#11786 bokeh 2.4.2 backports"

- **Change type:** Task (maintenance)
- **Change categorized:** Patch (minor)
- **Impacts:** This is a general backporting task; it doesn't describe specific changes but indicates that bug fixes or improvements from a later branch (likely the development branch for a future major/minor release) have been applied to the 2.4.2 release branch.
- **Backward compatibility:** No issues, backporting aims to maintain compatibility.
- **Simple explanations:**  Changes made in a newer version of Bokeh have been brought back to the 2.4.2 version.
- **Code examples:** N/A - this is a general maintenance task.
- **One-sentence summary:** Applied relevant changes from a later version to 2.4.2.
</change_breakdown>

<change_number>12</change_number>
<change_description>
This entry indicates a general maintenance task where changes (likely bug fixes, improvements, or small features) that were originally made in a later development branch of Bokeh (e.g., the branch for version 3.0) have been "backported" to the 2.4.2 release branch. Backporting is a common practice in software development to bring improvements and fixes to older, stable releases without requiring users to upgrade to a new major or minor version.
</change_description>

<code_example>
This is a general maintenance task, and there's no specific user-facing code example.
</code_example>

<simple_explanation>
Sometimes, developers make improvements or fix bugs in a newer version of Bokeh that's still under development. Backporting means taking those improvements and applying them to an older, stable version like 2.4.2. This way, users of the older version can benefit from the improvements without having to update to the newer, potentially less stable version.
</simple_explanation>

<change_breakdown>
> "#11790 [component: build] Bryanv/pin sphinx 42"

- **Change type:** Task (build dependency management)
- **Change categorized:** Patch (minor)
- **Impacts:** Affects the build process for Bokeh, specifically related to documentation generation.
- **Backward compatibility:** No issues.
- **Simple explanations:** The Sphinx version used to build Bokeh's documentation has been pinned to version 4.2, likely to avoid compatibility issues with newer or older versions.
- **Code examples:** N/A - this relates to build configuration.
- **One-sentence summary:** Set the Sphinx version to 4.2 for building documentation.
</change_breakdown>

<change_number>13</change_number>
<change_description>
This change modifies the Bokeh build process by "pinning" the version of Sphinx to 4.2. Sphinx is a widely used tool for generating documentation from Python code and reStructuredText or Markdown files. Pinning the version means specifying that only version 4.2 should be used, preventing automatic upgrades to newer versions that might introduce incompatibilities or unexpected changes in the generated documentation.
</change_description>

<code_example>
This is a build configuration change, and there's no user-facing code example. It would be reflected in the project's dependency specification files (e.g., `requirements.txt`, `environment.yml`, or similar).
</code_example>

<simple_explanation>
Bokeh uses a tool called Sphinx to create its documentation. This change makes sure that Bokeh always uses version 4.2 of Sphinx. It's like saying, "Always use this specific version of the tool, don't use any other version." This helps ensure that the documentation is always built correctly and looks the same way, even if newer versions of Sphinx come out.
</simple_explanation>

<change_breakdown>
> "#11797 Add OS to bokeh info"

- **Change type:** Task (feature enhancement)
- **Change categorized:** Patch (minor)
- **Impacts:** Improves the `bokeh info` command by providing more system information.
- **Backward compatibility:** No issues.
- **Simple explanations:** The `bokeh info` command now displays the operating system, which is helpful for debugging.
- **Code examples:** N/A - relates to the `bokeh info` command-line output.
- **One-sentence summary:** Enhanced the `bokeh info` command to include operating system information.
</change_breakdown>

<change_number>14</change_number>
<change_description>
This change enhances the `bokeh info` command-line tool. This command is used to display information about the installed Bokeh version and its environment, which can be helpful for debugging or troubleshooting. This specific change adds the operating system information to the output, providing more context about the user's system.
</change_description>

<code_example>
This change affects the output of the `bokeh info` command. There's no user-facing Python code example.
**Example of running `bokeh info` before the change:**

```
Python version      :  3.9.7
Bokeh version       :  2.4.1
BokehJS version     :  2.4.1
node.js version     :  v14.17.6
npm version         :  6.14.15
```

**Example of running `bokeh info` after the change:**

```
Python version      :  3.9.7
Bokeh version       :  2.4.2
BokehJS version     :  2.4.2
Operating system    :  Windows-10-10.0.19041-SP0
node.js version     :  v14.17.6
npm version         :  6.14.15
```
</code_example>

<simple_explanation>
Bokeh has a command called `bokeh info` that tells you about your Bokeh installation. This change makes that command show you what operating system you're using (like Windows, macOS, or Linux). This can be helpful if you're having problems with Bokeh and need to report a bug, as it gives the developers more information about your system.
</simple_explanation>

<change_breakdown>
> "#11805 More 3.0 -> 2.4.2 backports"

- **Change type:** Task (maintenance)
- **Change categorized:** Patch (minor)
- **Impacts:** Similar to "#11786", this indicates further backporting of changes from the 3.0 development branch to the 2.4.2 release.
- **Backward compatibility:** No issues, backporting aims to maintain compatibility.
- **Simple explanations:** More changes from the newer Bokeh version have been brought to the 2.4.2 version.
- **Code examples:** N/A - this is a general maintenance task.
- **One-sentence summary:** Applied more relevant changes from version 3.0 to 2.4.2.
</change_breakdown>

<change_number>15</change_number>
<change_description>
This entry, similar to "#11786," indicates another round of backporting changes from the Bokeh 3.0 development branch to the stable 2.4.2 release. This suggests that the Bokeh developers continued to identify bug fixes, improvements, or small features in the newer development version that were suitable for inclusion in the older release.
</change_description>

<code_example>
This is a general maintenance task, and there's no specific user-facing code example.
</code_example>

<simple_explanation>
This is similar to change #12. Developers have taken more improvements or bug fixes from the newer version of Bokeh (3.0, which is still being developed) and applied them to the older, stable version (2.4.2). This makes the older version better without requiring users to upgrade.
</simple_explanation>

<change_breakdown>
> "#11810 [component: docs] Update docs for new issue forms"

- **Change type:** Task (documentation update)
- **Change categorized:** Patch (minor)
- **Impacts:** Updates the documentation to reflect the changes in the GitHub issue reporting process (related to "#11791").
- **Backward compatibility:** No issues.
- **Simple explanations:** The documentation has been updated to explain how to use the new GitHub issue forms.
- **Code examples:** N/A - this is a documentation update.
- **One-sentence summary:** Updated the documentation to reflect the new GitHub issue forms.
</change_breakdown>

<change_number>16</change_number>
<change_description>
This change updates the Bokeh documentation to provide instructions on using the new GitHub issue forms, which were introduced in change "#11791." The updated documentation will likely guide users on how to properly fill out the forms, what information is required for different types of issues, and any other relevant details about the new issue reporting process.
</change_description>

<code_example>
This is a documentation update, and there's no user-facing code example. The updated documentation on the Bokeh website will reflect this change.
</code_example>

<simple_explanation>
Since the way you report problems on GitHub has changed (see change #7), the Bokeh documentation has been updated to explain how to use the new system. It's like updating a user manual when a product gets a new feature.
</simple_explanation>

<change_breakdown>
> "#11824 Updates for release"

- **Change type:** Task (general release preparation)
- **Change categorized:** Patch (minor)
- **Impacts:** This is a general entry indicating various updates made in preparation for the 2.4.2 release. It doesn't specify particular changes.
- **Backward compatibility:** No issues.
- **Simple explanations:** Various small changes were made to get Bokeh ready for the 2.4.2 release.
- **Code examples:** N/A - this is a general release preparation task.
- **One-sentence summary:** Made final updates in preparation for the 2.4.2 release.
</change_breakdown>

<change_number>17</change_number>
<change_description>
This entry is a general placeholder for various updates made in preparation for the release of Bokeh 2.4.2. These updates could include things like updating version numbers, finalizing documentation, running final tests, and other tasks necessary to ensure a smooth release.
</change_description>

<code_example>
This is a general release preparation task, and there's no specific user-facing code example.
</code_example>

<simple_explanation>
Before a new version of Bokeh is released,

Okay, let's break down this Bokeh changelog, version by version, and provide clear explanations for each change.

## Bokeh 1.4.0 (Released 2019-11-04)

### Bug Fixes

<change_breakdown>
- **Change quoted:** "#8402 [component: bokehjs] No clean way to update vbar_stack"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users trying to update stacked vertical bar charts dynamically.
- **Backward compatibility:**  Fixes previous incorrect behavior, should not break existing code unless it relied on the buggy behavior.
- **Simple explanations:**  There was no proper method to refresh the data in stacked bar charts.
- **Code examples:** Show how to correctly update `vbar_stack` after the fix.
- **One-sentence summary:** This fixes an issue where stacked vertical bar charts could not be easily updated with new data.
</change_breakdown>

<change_number>1</change_number>
<change_description>
Previously, there was no straightforward way to update the data displayed in a stacked vertical bar chart (`vbar_stack`). This bug fix introduces a mechanism that allows for a clean update of the data, making it easier to create dynamic and interactive stacked bar charts.
</change_description>

<code_example>
```python
# Before the fix, updating vbar_stack was problematic.
# After the fix:

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Sample data
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]
exports = {'fruits': fruits,
           '2015': [2, 1, 4, 3, 2, 4],
           '2016': [5, 3, 4, 2, 4, 6],
           '2017': [3, 2, 4, 4, 5, 3]}

# Create a ColumnDataSource
source = ColumnDataSource(data=exports)

# Create the plot
p = figure(x_range=fruits, title="Fruit Exports by Year",
           toolbar_location=None, tools="")

# Add vbar_stack
p.vbar_stack(years, x='fruits', width=0.9, color=["#c9d9d3", "#718dbf", "#e84d60"], source=source,
             legend_label=years)

# To update the data:
new_data = {'fruits': fruits,
           '2015': [3, 2, 5, 4, 3, 5],
           '2016': [6, 4, 3, 3, 5, 7],
           '2017': [4, 3, 3, 5, 6, 2]}
source.data = new_data 

show(p)
```
</code_example>

<simple_explanation>
Imagine you have a stacked bar chart showing fruit exports over several years. Before, if you wanted to update the chart with new export data, it was messy and didn't work well. This fix makes it simple: you just update the data source, and the chart refreshes correctly.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#8778 [component: bokehjs] Hover over image is showing wrong @image tooltip on flipped axis"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users who use hover tooltips with images on plots where the axis is flipped (e.g., x-axis going from right to left).
- **Backward compatibility:** Fixes incorrect behavior; should not negatively impact existing code.
- **Simple explanations:** Hover tooltips were showing incorrect information when the axis direction was reversed for image plots.
- **Code examples:** Demonstrate an image plot with a flipped axis and show that the hover tooltip now displays the correct information.
- **One-sentence summary:** This fixes a bug where hover tooltips on images displayed incorrect data when one of the axes was flipped.
</change_breakdown>

<change_number>2</change_number>
<change_description>
This bug fix addresses an issue where the hover tooltip displayed incorrect `@image` values when hovering over an image plot with a flipped axis. A flipped axis means the axis is reversed (e.g., the x-axis runs from right to left instead of left to right). The fix ensures that the correct image data is shown in the tooltip regardless of the axis orientation.
</change_description>

<code_example>
```python
# The example is conceptual because creating a scenario 
# that reliably reproduces the original bug is complex.
# This demonstrates the intended behavior after the fix.

from bokeh.plotting import figure, show
from bokeh.models import HoverTool
import numpy as np

# Create sample image data
img = np.random.randint(0, 255, size=(100, 100))

# Create a plot with a flipped x-axis
p = figure(x_range=(100, 0), y_range=(0, 100), width=400, height=400,
           tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])

# Add the image
p.image(image=[img], x=0, y=0, dw=100, dh=100, palette="Spectral11")

# Add a hover tool
hover = HoverTool(tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])
p.add_tools(hover)

show(p)
# Now, when you hover over the image, the tooltip should 
# correctly show the image value at that point, even though the x-axis is flipped.
```
</code_example>

<simple_explanation>
Think of a picture on a graph. If you flipped the graph sideways, the information that popped up when you hovered over the picture got mixed up. This fix makes sure the correct information shows up, no matter how the graph is flipped.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#8976 [component: bokehjs] [bug] geographical plots cannot be saved with the save tool"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users trying to save geographical plots using the built-in save tool.
- **Backward compatibility:** Fixes a previously broken feature; should not introduce any backward compatibility issues.
- **Simple explanations:**  The save tool was not working correctly for geographical plots.
- **Code examples:** Demonstrate a geographical plot and show that it can now be saved correctly using the save tool.
- **One-sentence summary:** This fixes an issue where geographical plots could not be saved using the Bokeh save tool.
</change_breakdown>

<change_number>3</change_number>
<change_description>
This change addresses a bug where the built-in save tool in Bokeh did not function correctly for geographical plots, such as those created using `gmap`. After this fix, users can now successfully save their geographical visualizations using the save tool, just like they can with other plot types.
</change_description>

<code_example>
```python
# Before the fix, saving a gmap plot with the save tool might not work.
# After the fix:

from bokeh.plotting import gmap, show
from bokeh.models import GMapOptions, ColumnDataSource
from bokeh.io import output_file

# Replace with your Google Maps API key
api_key = "YOUR_GOOGLE_MAPS_API_KEY" 

# output to static HTML file
output_file("gmap_plot_save_example.html")

# Define map options
map_options = GMapOptions(lat=37.7749, lng=-122.4194, map_type="roadmap", zoom=11)

# Create the plot
p = gmap(api_key, map_options, title="San Francisco", width=600, height=400)

# add a circle on top
lat = [37.75, 37.78, 37.81]
lon = [-122.40, -122.44, -122.48]
source = ColumnDataSource(data=dict(lat=lat, lon=lon))
p.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, source=source)

# Add the save tool (it's included by default, but we show it here for clarity)
# from bokeh.models import SaveTool
# p.add_tools(SaveTool())

show(p)
# You should now be able to save this geographical plot using the save tool.
```
</code_example>

<simple_explanation>
Imagine you made a map using Bokeh. Before, if you tried to save it using the save button, it wouldn't work. This fix makes the save button work correctly for maps.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9035 [component: bokehjs] [widgets] [bug] spinner only considers 1 decimal"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users of the `Spinner` widget who need more than one decimal place of precision.
- **Backward compatibility:** Fixes a limitation; existing code using `Spinner` might display more decimal places now.
- **Simple explanations:** The `Spinner` widget was limited to only handling numbers with one decimal place.
- **Code examples:** Demonstrate a `Spinner` widget now handling multiple decimal places.
- **One-sentence summary:** This fixes a bug where the `Spinner` widget could only handle numbers with a single decimal place, now allowing for greater precision.
</change_breakdown>

<change_number>4</change_number>
<change_description>
The `Spinner` widget, which provides a text box with up/down arrows to increment or decrement a numerical value, was previously limited to only one decimal place of precision. This bug fix removes that limitation, allowing the `Spinner` to handle numbers with multiple decimal places, as specified by the `step` property.
</change_description>

<code_example>
```python
from bokeh.models.widgets import Spinner
from bokeh.io import curdoc

# Before the fix, the Spinner might have rounded to only one decimal place.
# After the fix:

# Create a Spinner widget with a step of 0.01
spinner = Spinner(title="Value (step=0.01)", low=0.0, high=1.0, step=0.01, value=0.5)

# Add the Spinner to the document
curdoc().add_root(spinner)

# you can run this example using bokeh serve
# bokeh serve --show myapp.py (assuming the code is saved in myapp.py)
# Now the Spinner will correctly handle values with two decimal places.
```
</code_example>

<simple_explanation>
Think of a number input box with little up and down arrows. Before, this box (the `Spinner`) could only handle numbers like 1.2 or 3.4 (one number after the dot). This fix lets it handle numbers with more digits after the dot, like 1.23 or 3.45, making it more precise.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9129 [component: bokehjs] [widgets] [bug] datepicker displayed value is not updating correctly"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users of the `DatePicker` widget where the displayed date did not always match the internal value.
- **Backward compatibility:** Fixes incorrect behavior; should not break existing code but might change the displayed date if it was previously incorrect.
- **Simple explanations:** The `DatePicker` widget sometimes showed the wrong date.
- **Code examples:** Show a `DatePicker` widget now correctly updating its displayed value.
- **One-sentence summary:** This fixes a bug where the `DatePicker` widget did not always display the currently selected date correctly.
</change_breakdown>

<change_number>5</change_number>
<change_description>
This change addresses a bug where the `DatePicker` widget did not consistently update its displayed value to reflect the currently selected date. This could lead to confusion where the user selects a date, but the widget continues to display a different date. After the fix, the displayed date will always accurately reflect the internal value of the `DatePicker`.
</change_description>

<code_example>
```python
from bokeh.models.widgets import DatePicker
from bokeh.io import curdoc
from bokeh.layouts import column
from datetime import date

# Create a DatePicker widget
date_picker = DatePicker(title="Select date", value=date(2019, 9, 20), min_date=date(2019, 9, 1), max_date=date(2020, 12, 31))

# to demonstrate the fix, let's add a callback that prints the selected date
def date_picker_changed(attrname, old, new):
    print(f"Date changed to: {date_picker.value}")

date_picker.on_change('value', date_picker_changed)

# Add the DatePicker to the document
curdoc().add_root(column(date_picker))

# you can run this example using bokeh serve
# bokeh serve --show myapp.py (assuming the code is saved in myapp.py)
# Now the DatePicker will always display the correct selected date, and the callback
# will print the updated date to the console.
```
</code_example>

<simple_explanation>
Imagine a calendar widget where you pick a date. Before, sometimes the date shown on the widget didn't change even when you picked a new one. This fix makes sure the date you pick is always the date you see on the widget.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9136 [component: bokehjs] Inner_width and inner_height not available after display"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users who need to access the `inner_width` and `inner_height` properties of a plot after it's displayed, particularly in layouts.
- **Backward compatibility:** Fixes a bug where these properties were not accessible; should not break existing code but might require adjustments if code was written to work around the bug.
- **Simple explanations:** The `inner_width` and `inner_height` properties, which represent the dimensions of the plot area excluding axes and titles, were not correctly calculated after the plot was rendered.
- **Code examples:** Show how to access `inner_width` and `inner_height` after the plot is displayed.
- **One-sentence summary:** This fixes an issue where the `inner_width` and `inner_height` properties of a plot were not available after the plot was displayed.
</change_breakdown>

<change_number>6</change_number>
<change_description>
This bug fix ensures that the `inner_width` and `inner_height` properties of a plot are correctly calculated and accessible after the plot has been displayed. These properties represent the dimensions of the plotting area itself, excluding the space occupied by axes, titles, and other elements.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import CustomJS
from bokeh.io import output_notebook

output_notebook()

# Create a plot
p = figure(width=400, height=200, title="Accessing Inner Width and Height")

# Add a circle
p.circle([1, 2, 3], [4, 5, 6])

# CustomJS to access inner_width and inner_height after rendering
callback = CustomJS(args=dict(p=p), code="""
    console.log('Inner Width:', p.inner_width);
    console.log('Inner Height:', p.inner_height);
""")

# Trigger the callback after the plot is displayed (e.g., with a tap tool)
p.js_on_event('tap', callback) 

show(p)
# After the fix, clicking on the plot will log the inner_width and inner_height
# to the browser's JavaScript console.
```
</code_example>

<simple_explanation>
Think of a plot like a picture frame. The `inner_width` and `inner_height` are the dimensions of the picture inside the frame, not including the frame itself. Before, these dimensions weren't available after the picture was displayed. This fix makes sure you can get these dimensions anytime, even after the plot is shown.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9143 [component: docs] [bug] roadmap link on docs page links to a nonexistent page"
- **Change type:** Bug fix (Documentation)
- **Change categorized:** Patch
- **Impacts:** Affects users trying to access the project roadmap from the documentation.
- **Backward compatibility:** No backward compatibility issues, as this only fixes a broken link.
- **Simple explanations:** The link to the project roadmap in the documentation was broken.
- **Code examples:** N/A - Documentation fix.
- **One-sentence summary:** This fixes a broken link to the project roadmap in the Bokeh documentation.
</change_breakdown>

<change_number>7</change_number>
<change_description>
This change corrects a broken link in the Bokeh documentation. Previously, the link to the project roadmap on the documentation page was pointing to a non-existent page. This fix ensures that the link now directs users to the correct roadmap.
</change_description>

<code_example>
N/A - This is a documentation fix, not a code change.
</code_example>

<simple_explanation>
It's like a broken link on a website. The link to the "future plans" page of Bokeh's documentation didn't work. This fix makes the link work again so you can see what's coming next for Bokeh.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9152 [component: bokehjs] [bug] hover tooltip breaks with full-circle wedge"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users using hover tooltips with full-circle wedge glyphs.
- **Backward compatibility:** Fixes incorrect behavior; should not negatively impact existing code.
- **Simple explanations:** Hover tooltips were not working correctly when used with wedges that formed a complete circle.
- **Code examples:** Demonstrate a full-circle wedge with a hover tooltip, showing that it now works correctly.
- **One-sentence summary:** This fixes an issue where hover tooltips did not function properly on full-circle wedge glyphs.
</change_breakdown>

<change_number>8</change_number>
<change_description>
This bug fix addresses an issue where hover tooltips were not functioning correctly when used with full-circle wedge glyphs. A full-circle wedge is a wedge where the start and end angles encompass a complete 360-degree rotation. After this fix, hover tooltips will display the correct information when hovering over these full-circle wedges.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import HoverTool
from bokeh.io import output_file

# output to static HTML file
output_file("full_circle_wedge_hover_fix.html")

# Create a plot
p = figure(width=400, height=400, tools="", title="Full-Circle Wedge Hover")

# Add a full-circle wedge (start_angle=0, end_angle=2*pi)
p.wedge(x=0, y=0, radius=1, start_angle=0, end_angle=6.28, color="navy", alpha=0.6,
        legend_label="Full Circle")

# Add a hover tool
hover = HoverTool(tooltips=[("Radius", "@radius"), ("Start Angle", "@start_angle"), ("End Angle", "@end_angle")])
p.add_tools(hover)

show(p)
# Now, when you hover over the full-circle wedge, the tooltip should display 
# the correct information.
```
</code_example>

<simple_explanation>
Imagine you have a pie chart that's a complete circle (a full pie). Before, if you hovered your mouse over it to see more information (like with a tooltip), it didn't work properly. This fix makes the information pop up correctly when you hover over a full-circle pie chart.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9174 [component: bokehjs] [bug] nan_color argument in linearcolormapper is not used"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users using `LinearColorMapper` to color data points with NaN values.
- **Backward compatibility:** Fixes a bug where the `nan_color` was ignored; now, NaN values will be colored according to the specified `nan_color`. Might change the appearance of plots if they contained NaN values.
- **Simple explanations:** The `LinearColorMapper` did not correctly color data points that had NaN (Not a Number) values, even if a `nan_color` was specified.
- **Code examples:** Demonstrate a `LinearColorMapper` now correctly coloring NaN values with the specified `nan_color`.
- **One-sentence summary:** This fixes a bug where the `LinearColorMapper` did not use the specified `nan_color` for NaN values, ensuring they are now colored correctly.
</change_breakdown>

<change_number>9</change_number>
<change_description>
This bug fix ensures that the `LinearColorMapper` correctly applies the specified `nan_color` to data points with NaN (Not a Number) values. Previously, the `nan_color` argument was ignored, and NaN values might have been rendered with a default color or not rendered at all.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import LinearColorMapper, ColumnDataSource
from bokeh.io import output_file
import numpy as np

# output to static HTML file
output_file("linear_color_mapper_nan_color_fix.html")

# Create sample data with some NaN values
data = {'x': [1, 2, 3, 4, 5],
        'y': [2, 5, np.nan, 8, 10],
        'value': [10, 20, np.nan, 40, 50]}
source = ColumnDataSource(data)

# Create a LinearColorMapper with a specified nan_color
mapper = LinearColorMapper(palette="Viridis256", low=0, high=50, nan_color="red")

# Create a plot
p = figure(width=400, height=400, title="LinearColorMapper NaN Color Fix")

# Add circles colored by the 'value' column, using the mapper
p.circle(x='x', y='y', size=20, source=source, color={'field': 'value', 'transform': mapper})

show(p)
# Now, the point with the NaN value will be colored red, as specified by nan_color.
```
</code_example>

<simple_explanation>
Imagine you're coloring points on a graph based on their values. If a point has a missing value (NaN), you want to color it differently, say, red. Before, even if you said to color NaN points red, it didn't work. This fix makes sure NaN points get the color you specified.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9185 [component: bokehjs] [regression] [bug] exporting google maps pngs sometimes not working properly"
- **Change type:** Bug fix (Regression)
- **Change categorized:** Patch
- **Impacts:** Affects users trying to export Google Maps plots as PNG images.
- **Backward compatibility:** Fixes a regression introduced in a previous version; should restore the previous functionality of exporting Google Maps plots to PNG.
- **Simple explanations:** Exporting Google Maps plots to PNG images was unreliable or broken in recent versions.
- **Code examples:** N/A - Difficult to demonstrate without a reliable way to reproduce the original bug. The fix ensures that the export functionality works as intended.
- **One-sentence summary:** This fixes a recent issue where exporting Google Maps plots as PNG images was not working reliably.
</change_breakdown>

<change_number>10</change_number>
<change_description>
This change addresses a regression where exporting Google Maps plots as PNG images was not working reliably. The issue likely arose from changes in recent Bokeh versions, and this fix restores the functionality to how it worked before the regression was introduced. Users should now be able to consistently export their Google Maps plots to PNG format.
</change_description>

<code_example>
```python
# This is a conceptual example, as reproducing the exact bug is difficult.
# The fix ensures that exporting a gmap plot to PNG works as expected.

from bokeh.plotting import gmap, show
from bokeh.io import export_png, output_file

# Replace with your Google Maps API key
api_key = "YOUR_GOOGLE_MAPS_API_KEY"

# output to static HTML file
output_file("gmap_export_png_example.html")

# Define map options
map_options = GMapOptions(lat=37.7749, lng=-122.4194, map_type="roadmap", zoom=11)

# Create the plot
p = gmap(api_key, map_options, title="San Francisco")

# Export the plot to PNG
export_png(p, filename="gmap_plot.png")

# show the plot
show(p)
# The export_png function should now reliably create a PNG image of the gmap plot.
```
</code_example>

<simple_explanation>
Think of taking a screenshot of a map you made with Bokeh. In some recent versions, trying to save that map as a picture (PNG) didn't always work. This fix makes sure you can save your map as a picture reliably again.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9240 [component: build] [bug] building custom extension breaks in notebook"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects developers creating custom Bokeh extensions and trying to use them within Jupyter notebooks.
- **Backward compatibility:** Fixes a build process issue; should not affect backward compatibility but will enable previously broken workflows.
- **Simple explanations:**  Building custom extensions for use in Jupyter notebooks was not working correctly.
- **Code examples:** N/A - This is a build process fix and doesn't lend itself to a simple code example within the context of using Bokeh.
- **One-sentence summary:** This fixes an issue where building custom Bokeh extensions for use in Jupyter notebooks was failing.
</change_breakdown>

<change_number>11</change_number>
<change_description>
This change addresses a bug in the build process for custom Bokeh extensions, specifically when those extensions were intended for use within Jupyter notebooks. The fix ensures that the build process completes successfully, allowing developers to create and use their custom extensions in notebooks without encountering errors related to the build.
</change_description>

<code_example>
N/A - This is related to the Bokeh extension build process, which is more complex to demonstrate in a simple code example. The fix ensures that developers can follow the standard procedures for building custom extensions, and those extensions will then work correctly within a Jupyter notebook environment.
</code_example>

<simple_explanation>
Imagine you're building a special add-on for Bokeh to use in Jupyter notebooks. Before, the building process for this add-on was broken. This fix makes sure you can build your add-on correctly so it works in your notebooks.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9266 [component: bokehjs] [widgets] [bug] datatable sorting broken"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users who rely on the sorting functionality of `DataTable` widgets.
- **Backward compatibility:** Fixes a previously broken feature; should not introduce backward compatibility issues.
- **Simple explanations:** The sorting functionality in `DataTable` widgets was not working correctly.
- **Code examples:** Demonstrate a `DataTable` where sorting now functions as expected.
- **One-sentence summary:** This fixes an issue where sorting data within a `DataTable` widget did not work properly.
</change_breakdown>

<change_number>12</change_number>
<change_description>
This bug fix addresses an issue where the sorting functionality of the `DataTable` widget was not working correctly. Users might have experienced incorrect sorting order, or the table might not have responded to sorting clicks at all. After this fix, clicking on column headers in a `DataTable` will correctly sort the data based on that column, in ascending or descending order.
</change_description>

<code_example>
```python
from bokeh.models import ColumnDataSource, DataTable, TableColumn
from bokeh.io import curdoc
from bokeh.layouts import column

# Sample data
data = {'col1': [1, 5, 3, 2, 4],
        'col2': ['apple', 'banana', 'orange', 'grape', 'kiwi'],
        'col3': [1.1, 5.5, 3.3, 2.2, 4.4]}
source = ColumnDataSource(data)

# Create columns
columns = [
    TableColumn(field="col1", title="Column 1"),
    TableColumn(field="col2", title="Column 2"),
    TableColumn(field="col3", title="Column 3"),
]

# Create a DataTable
data_table = DataTable(source=source, columns=columns, width=400, height=200, sortable=True)

# Add the DataTable to the document
curdoc().add_root(column(data_table))

# you can run this example using bokeh serve
# bokeh serve --show myapp.py (assuming the code is saved in myapp.py)
# Now, clicking on the column headers in the DataTable will correctly sort the data.
```
</code_example>

<simple_explanation>
Imagine you have a table of data in your Bokeh application. Before, if you tried to sort the table by clicking on a column header (like sorting numbers from smallest to largest), it didn't work. This fix makes the sorting work correctly again.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9267 [component: bokehjs] [bug] range_tool selection is over-responsive in y direction"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users using the `RangeTool` to select a range on a plot.
- **Backward compatibility:** Fixes an issue with oversensitivity; should not break existing code but will make the `RangeTool` behave more predictably.
- **Simple explanations:** The `RangeTool` was too sensitive in the vertical direction, making it difficult to select the desired range accurately.
- **Code examples:** N/A - Difficult to demonstrate visually in a code example. The fix makes the `RangeTool`'s behavior more intuitive and less "jumpy."
- **One-sentence summary:** This fixes a bug where the `RangeTool` was overly sensitive in the y-direction, making it easier to use for selecting ranges.
</change_breakdown>

<change_number>13</change_number>
<change_description>
This bug fix addresses an issue where the `RangeTool` was overly sensitive when selecting a range in the vertical (y) direction. This oversensitivity made it difficult for users to precisely select the desired range. The fix adjusts the responsiveness of the `RangeTool` to make it more intuitive and easier to use, particularly when adjusting the vertical bounds of the selection.
</change_description>

<code_example>
```python
# This is a conceptual example, as the bug's effect is more about user experience
# than something easily demonstrable in static code.
# The fix makes the RangeTool less "jumpy" in the y-direction.

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.layouts import column
from bokeh.io import output_file
import numpy as np

# output to static HTML file
output_file("range_tool_sensitivity_fix.html")

# Sample data
x = np.linspace(0, 10, 500)
y = np.sin(x)

source = ColumnDataSource(data=dict(x=x, y=y))

# Create the main plot
p = figure(height=300, width=800, tools="xpan", toolbar_location=None,
           x_axis_type="datetime", x_axis_location="above",
           background_fill_color="#efefef", x_range=(x[150], x[250]))

p.line('x', 'y', source=source)
p.yaxis.axis_label = 'Price'

# Create a plot for the RangeTool
select = figure(title="Drag the middle and edges of the selection box to change the range above",
                height=130, width=800, y_range=p.y_range,
                x_axis_type="datetime", y_axis_type=None,
                tools="", toolbar_location=None, background_fill_color="#efefef")

# Create the RangeTool
range_tool = RangeTool(x_range=p.x_range)
range_tool.overlay.fill_color = "navy"
range_tool.overlay.fill_alpha = 0.2

select.line('x', 'y', source=source)
select.ygrid.grid_line_color = None
select.add_tools(range_tool)
select.toolbar.active_multi = range_tool

show(column(p, select))
# The RangeTool should now be less sensitive in the y-direction, making it easier to use.
```
</code_example>

<simple_explanation>
Imagine you have a tool that lets you select a part of a graph. Before, this tool (the `RangeTool`) was too sensitive when you moved it up and down, making it hard to select exactly what you wanted. This fix makes the tool less "jumpy" vertically, so it's easier to control.
</simple_explanation>

---

<change_breakdown>
- **Change quoted:** "#9309 [API: models] [component: docs] [bug] documentation panels empty"
- **Change type:** Bug fix (Documentation)
- **Change categorized:** Patch
- **Impacts:** Affects users trying to view documentation for certain Bokeh models.
- **Backward compatibility:** No backward compatibility issues; this fixes missing documentation.
- **Simple explanations:** Some parts of the Bokeh documentation were empty or missing.
- **Code examples:** N/A - Documentation fix.
- **One-sentence summary:** This fixes an issue where some

Okay, let's break down this changelog for Bokeh-Visualization, explaining each change in detail and making it easy for everyone to understand.

# Bokeh-Visualization Changelog Breakdown

## Version 3.0.3

### Bug Fixes

<change_breakdown>
- **Change quoted:** "#12583 [component: bokehjs] [BUG] Nested gridplot collapses figures"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users who create gridplots with nested structures. Previously, nested figures might have collapsed unexpectedly.
- **Backward compatibility:** No backward compatibility issues; this is a fix for existing functionality.
- **Simple explanations:** Imagine you're building a grid of plots, and inside one of those grid cells, you want another smaller grid. This bug caused the inner grid to disappear or shrink incorrectly.
- **Code examples:**
  ```python
  from bokeh.plotting import figure, gridplot, show
  
  p1 = figure(width=200, height=200)
  p1.circle([1, 2, 3], [4, 5, 6])
  p2 = figure(width=200, height=200)
  p2.line([1, 2, 3], [6, 5, 4])
  
  inner_grid = gridplot([[p1, p2]], width=200, height=200)
  outer_grid = gridplot([[inner_grid, figure(width=200, height=200)]])
  
  show(outer_grid)  # Before the fix, inner_grid might have collapsed.
  ```
- **One-sentence summary:** This fix ensures that nested gridplots render correctly without collapsing figures.
</change_breakdown>

<change_number>1</change_number>
<change_description>
This bug fix addresses an issue where nested gridplots (grids within grids) would cause figures to collapse or disappear unexpectedly. The root cause was likely related to how BokehJS handled the layout and sizing of nested grid structures.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, gridplot, show

p1 = figure(width=200, height=200)
p1.circle([1, 2, 3], [4, 5, 6])
p2 = figure(width=200, height=200)
p2.line([1, 2, 3], [6, 5, 4])

inner_grid = gridplot([[p1, p2]], width=200, height=200)
outer_grid = gridplot([[inner_grid, figure(width=200, height=200)]])

show(outer_grid)
```
</code_example>

<simple_explanation>
Imagine you have a big box (outer grid), and inside it, you put a smaller box (inner grid) with two toys (figures). This bug was like the smaller box suddenly shrinking and hiding the toys. The fix makes sure the smaller box stays the right size and keeps the toys visible.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12611 [BUG] `get_screenshot_as_png`"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users who use the `get_screenshot_as_png` function to capture plot images.
- **Backward compatibility:** No backward compatibility issues; this is a fix for existing functionality.
- **Simple explanations:** The `get_screenshot_as_png` function was likely not working as expected in certain scenarios, potentially returning an error or an incorrect image.
- **Code examples:**
  ```python
  from bokeh.io import get_screenshot_as_png
  from bokeh.plotting import figure, show
  
  p = figure()
  p.circle([1, 2], [3, 4])
  show(p)
  
  image = get_screenshot_as_png(p)
  # image.save("my_plot.png") # Save the screenshot (requires Pillow)
  ```
- **One-sentence summary:** This fix ensures the `get_screenshot_as_png` function reliably captures plot screenshots.
</change_breakdown>

<change_number>2</change_number>
<change_description>
This bug fix resolves issues with the `get_screenshot_as_png` function, which is used to capture a screenshot of a Bokeh plot or layout as a PNG image. The exact nature of the bug isn't specified, but it likely involved errors or incorrect output when trying to capture screenshots.
</change_description>

<code_example>
```python
from bokeh.io import get_screenshot_as_png
from bokeh.plotting import figure, show

p = figure()
p.circle([1, 2], [3, 4])
show(p) # need to show at least once.

image = get_screenshot_as_png(p)
# image.save("my_plot.png") # Save the screenshot (requires Pillow)
```
</code_example>

<simple_explanation>
Think of `get_screenshot_as_png` as taking a picture of your plot. This bug was like the camera sometimes not working properly, either giving you a blurry picture or no picture at all. The fix ensures the camera works correctly every time.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12627 [BUG] sizing_mode="stretch_both" fails since 3.0.0"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users who use `sizing_mode="stretch_both"` to make their plots automatically resize to fit the available space.
- **Backward compatibility:** No backward compatibility issues, but it restores functionality that was broken in 3.0.0.
- **Simple explanations:**  `sizing_mode="stretch_both"` is supposed to make a plot expand to fill the width and height of its container. Since version 3.0.0, this feature was not working correctly.
- **Code examples:**
  ```python
  from bokeh.plotting import figure, show
  from bokeh.layouts import column
  
  p = figure(sizing_mode="stretch_both")
  p.line([1, 2, 3], [4, 5, 6])
  
  layout = column(p, sizing_mode="stretch_both")
  show(layout)
  ```
- **One-sentence summary:** This fix restores the functionality of `sizing_mode="stretch_both"`, allowing plots to dynamically resize to their container's dimensions.
</change_breakdown>

<change_number>3</change_number>
<change_description>
This bug fix addresses a regression introduced in Bokeh 3.0.0 where setting `sizing_mode="stretch_both"` on a plot or layout would not make it expand to fill the available space as expected. This mode is useful for creating responsive plots that adjust to different screen sizes or window resizes.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.layouts import column

p = figure(sizing_mode="stretch_both")
p.line([1, 2, 3], [4, 5, 6])

layout = column(p, sizing_mode="stretch_both")
show(layout)
```
</code_example>

<simple_explanation>
Imagine you have a picture frame that can magically resize itself to fit any picture you put in it. `sizing_mode="stretch_both"` is like that magical frame for your plot. This bug made the frame stop resizing, but the fix makes it work again.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12633 [component: bokehjs] [BUG] Styles are not applied to model in Firefox"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users who use custom CSS styles with Bokeh models, specifically in the Firefox browser.
- **Backward compatibility:** No backward compatibility issues; this is a browser-specific fix.
- **Simple explanations:** Bokeh models were not receiving the intended CSS styles when viewed in Firefox.
- **Code examples:** This one is harder to demonstrate without a specific Bokeh model and CSS, but the general idea is that if you had CSS like `.my-bokeh-model { color: red; }` and a corresponding Bokeh model, the style wouldn't apply in Firefox.
- **One-sentence summary:** This fix ensures that custom CSS styles are correctly applied to Bokeh models in the Firefox browser.
</change_breakdown>

<change_number>4</change_number>
<change_description>
This is a browser-specific bug fix targeting Firefox. It appears that custom CSS styles intended for Bokeh models were not being applied correctly in this browser. The issue likely stemmed from differences in how Firefox handles CSS or interacts with BokehJS compared to other browsers.
</change_description>

<code_example>
While a precise code example is difficult without knowing the exact model and styles involved, the general problem can be illustrated conceptually:

```python
# In your Bokeh model definition (if you have a custom model)
# You might have something like:
# __css__ = ["my_styles.css"]

# And in my_styles.css:
# .my-bokeh-model {
#   color: red;
#   font-size: 16px;
# }
```

Before the fix, these styles might not have been applied to the `my-bokeh-model` elements when viewed in Firefox.
</code_example>

<simple_explanation>
Imagine you're giving instructions on how to dress up your toys (Bokeh models) using different clothes (CSS styles). This bug was like Firefox ignoring those instructions and dressing the toys in the default clothes. The fix makes sure Firefox listens to your instructions and dresses the toys correctly.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12640 [component: bokehjs] [BUG] Embedded plot not sized correctly if not visible from the start"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users embedding Bokeh plots that are initially hidden (e.g., inside a collapsed section or a tab that's not active).
- **Backward compatibility:** No backward compatibility issues; this is a fix for how initially hidden plots are handled.
- **Simple explanations:** If a plot was embedded but not immediately visible, its size might not have been calculated correctly when it became visible.
- **Code examples:**  Difficult to show a minimal example, but imagine a scenario where you have a plot inside a tab that's not the initially active tab. When you switch to that tab, the plot might not have the correct dimensions.
- **One-sentence summary:** This fix ensures that embedded Bokeh plots are sized correctly even if they are not visible when the page initially loads.
</change_breakdown>

<change_number>5</change_number>
<change_description>
This bug fix addresses an issue with how Bokeh plots are sized when they are initially hidden and then made visible. This could occur when a plot is embedded within a tab, a collapsed section, or any element that is not displayed when the page first loads. The bug likely caused the plot to have incorrect dimensions when it became visible.
</change_description>

<code_example>
A simple example is not easily constructed, but consider a scenario with tabs:

```python
from bokeh.models import Panel, Tabs
from bokeh.plotting import figure, show

p1 = figure(width=200, height=200)
p1.circle([1, 2], [3, 4])
tab1 = Panel(child=p1, title="Tab 1")

p2 = figure(width=200, height=200) # This plot is initially hidden
p2.line([1, 2], [3, 4])
tab2 = Panel(child=p2, title="Tab 2")

tabs = Tabs(tabs=[tab1, tab2])
show(tabs)
```

Before the fix, `p2` might not have rendered with the correct size when "Tab 2" was selected.
</code_example>

<simple_explanation>
Imagine you have a picture (plot) hidden in a drawer. When you open the drawer, you expect the picture to be the right size. This bug was like the picture being the wrong size when you first opened the drawer. The fix makes sure the picture is always the correct size, even if it was hidden initially.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12623 Ensure change callback manipulation is threadsafe"
- **Change type:** Bug fix
- **Change categorized:** Patch
- **Impacts:** Affects users working with Bokeh in multi-threaded environments, particularly when modifying change callbacks.
- **Backward compatibility:** No backward compatibility issues; this is a fix for thread safety.
- **Simple explanations:** In a multi-threaded context, manipulating change callbacks (functions that are called when a property changes) was not threadsafe, which could lead to race conditions or unexpected behavior.
- **Code examples:** Hard to provide a simple example without a specific multi-threaded scenario, but the general idea is that adding or removing callbacks while other threads are potentially accessing them could cause problems.
- **One-sentence summary:** This fix ensures that adding or removing change callbacks in Bokeh is safe to do in multi-threaded applications.
</change_breakdown>

<change_number>6</change_number>
<change_description>
This bug fix addresses a thread safety issue related to manipulating change callbacks in Bokeh. Change callbacks are functions that are executed when a specific property of a Bokeh model changes. In a multi-threaded environment, if multiple threads were simultaneously adding or removing callbacks, it could lead to race conditions or data corruption.
</change_description>

<code_example>
Demonstrating thread safety issues requires a multi-threaded example, which is beyond a simple illustration. However, the concept can be understood as follows:

```python
# Imagine a scenario where you're adding a callback in one thread:
# thread_1: slider.on_change('value', my_callback)

# And removing it in another thread:
# thread_2: slider.remove_on_change('value', my_callback)

# If these operations weren't threadsafe, it could lead to problems.
```
</code_example>

<simple_explanation>
Imagine you have a button (Bokeh model) that does something when you press it (change callback). If multiple people (threads) try to change what the button does at the same time, things can get messed up. This fix is like adding a rule that only one person can change the button's function at a time, preventing confusion.
</simple_explanation>

### Tasks

<change_breakdown>
- **Change quoted:** "#12591 [component: tests] Many `CoverageWarning: Couldn't parse (...)` in unit tests"
- **Change type:** Task (Test improvement)
- **Change categorized:** Patch (Development process improvement)
- **Impacts:** Improves the quality and reliability of Bokeh's test suite.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** The unit tests were producing warnings related to code coverage analysis, indicating potential issues in how tests were being parsed or analyzed.
- **Code examples:** Not applicable, as this is a test suite issue.
- **One-sentence summary:** This task addresses warnings in the unit tests related to code coverage, making the tests more reliable.
</change_breakdown>

<change_number>7</change_number>
<change_description>
This task focuses on improving the Bokeh test suite. The "CoverageWarning: Couldn't parse (...)" messages suggest that the code coverage tool (likely `coverage.py`) was having trouble analyzing certain test files. This could be due to syntax errors, incompatible code, or issues with how the tests were structured.
</change_description>

<code_example>
Not applicable, as this is a task related to the testing infrastructure, not user-facing code.
</code_example>

<simple_explanation>
Imagine you have a robot that checks your homework (tests). This task is like fixing the robot so it can properly read and understand all your homework, ensuring it doesn't miss any mistakes.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12595 [component: docs] More neutral install instructions"
- **Change type:** Task (Documentation improvement)
- **Change categorized:** Patch (Documentation quality)
- **Impacts:** Makes the installation instructions more accessible and less biased towards a specific method.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** The installation instructions were likely improved to be more neutral and inclusive of different installation methods (e.g., pip, conda).
- **Code examples:** Not applicable, as this is a documentation change.
- **One-sentence summary:** This task updates the installation instructions to be more neutral and user-friendly.
</change_breakdown>

<change_number>8</change_number>
<change_description>
This task involves updating the Bokeh installation documentation to be more "neutral." This likely means providing instructions for multiple installation methods (e.g., using `pip`, `conda`, or building from source) without favoring one over the others. It might also involve removing any potentially biased language or assumptions about the user's environment.
</change_description>

<code_example>
Not applicable, as this is a documentation change.
</code_example>

<simple_explanation>
Imagine you have a recipe book. This task is like rewriting the instructions to include different ways to make the same dish (e.g., using different types of ovens or ingredients), making the recipe more accessible to more people.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12607 output_notebook uses a deprecated API"
- **Change type:** Task (Code update)
- **Change categorized:** Patch (Internal code improvement)
- **Impacts:** Updates internal code to use non-deprecated APIs, potentially improving stability or compatibility.
- **Backward compatibility:** No direct user-facing impact, but might improve the behavior of `output_notebook`.
- **Simple explanations:** The `output_notebook` function (used for displaying Bokeh plots in Jupyter notebooks) was using an older, deprecated API. This task updates it to use a newer, recommended API.
- **Code examples:** Not applicable without knowing the specific deprecated API, but the general idea is that the internal implementation of `output_notebook` was modernized.
- **One-sentence summary:** This task updates the `output_notebook` function to use a current, non-deprecated API.
</change_breakdown>

<change_number>9</change_number>
<change_description>
This task involves updating the `output_notebook` function, which is used to display Bokeh plots within Jupyter notebooks. The function was using a deprecated API, meaning an older method or interface that is no longer recommended for use. This task likely replaced the deprecated API with a newer, supported one.
</change_description>

<code_example>
Not applicable without knowing the specific deprecated API. However, the change would be internal to the `output_notebook` function's implementation and would not affect how users call it:

```python
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook() # This call remains the same

p = figure()
p.circle([1, 2], [3, 4])
show(p)
```
</code_example>

<simple_explanation>
Imagine you have a remote control (output_notebook) that uses old, outdated batteries (deprecated API). This task is like replacing those old batteries with new, better ones, making the remote control work more reliably.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12608 models.util.structure uses deprecated API"
- **Change type:** Task (Code update)
- **Change categorized:** Patch (Internal code improvement)
- **Impacts:** Updates internal code to use non-deprecated APIs, likely improving code maintainability and stability.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** Similar to the previous task, this one involves updating internal code within the `models.util.structure` module to use a current, non-deprecated API.
- **Code examples:** Not applicable, as this is an internal code change.
- **One-sentence summary:** This task modernizes the internal code in `models.util.structure` by replacing a deprecated API with a current one.
</change_breakdown>

<change_number>10</change_number>
<change_description>
This task focuses on updating the internal code within the `bokeh.models.util.structure` module. This module likely contains utility functions or classes used internally by Bokeh. It was using a deprecated API, which has been replaced with a newer, recommended alternative.
</change_description>

<code_example>
Not applicable, as this change is internal to Bokeh and does not affect user-facing code.
</code_example>

<simple_explanation>
This is similar to the previous task but in a different part of the Bokeh library. It's like upgrading an old, worn-out part in a machine with a new, improved part, making the machine run smoother overall.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12641 [component: docs] Links to many examples are out of date"
- **Change type:** Task (Documentation fix)
- **Change categorized:** Patch (Documentation quality)
- **Impacts:** Improves the user experience by ensuring that links to examples in the documentation are correct.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** Some links to examples within the Bokeh documentation were broken or outdated. This task fixes those links.
- **Code examples:** Not applicable, as this is a documentation change.
- **One-sentence summary:** This task updates broken or outdated links in the documentation, making it easier for users to find relevant examples.
</change_breakdown>

<change_number>11</change_number>
<change_description>
This task involves fixing broken or outdated links within the Bokeh documentation, specifically those pointing to examples. This improves the user experience by ensuring that users can easily access the examples referenced in the documentation.
</change_description>

<code_example>
Not applicable, as this is a documentation change.
</code_example>

<simple_explanation>
Imagine you have a textbook with links to websites for more information. This task is like updating all the broken links in the textbook so that they point to the correct websites again.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12646 [FEATURE] Add a find_stack_level to deprecation.py"
- **Change type:** Task (Feature - internal utility)
- **Change categorized:** Patch (Development process improvement)
- **Impacts:** Improves the accuracy or usefulness of deprecation warnings by providing more context about where the deprecated function was called from.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** The `deprecation.py` module likely contains utilities for handling deprecation warnings. Adding a `find_stack_level` function would help pinpoint the location in the code where a deprecated function is being used.
- **Code examples:** Not applicable, as this is an internal utility function.
- **One-sentence summary:** This task adds a utility function to help identify the source of deprecation warnings more easily.
</change_breakdown>

<change_number>12</change_number>
<change_description>
This task adds a new function, `find_stack_level`, to the internal `deprecation.py` module. This module likely contains utilities for managing deprecation warnings within Bokeh. The new function is designed to help determine the stack level (i.e., the location in the code's call stack) from which a deprecated function is being called. This can make it easier to track down and update deprecated code.
</change_description>

<code_example>
Not applicable, as this is an internal utility function that would be used by Bokeh's deprecation warning system, not directly by users.
</code_example>

<simple_explanation>
Imagine you have a tool that tells you when you're using an old, outdated method (deprecation warning). This task is like adding a feature to that tool that also tells you exactly where in your work you're using that outdated method, making it easier to fix.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12351 Updates to Docker image building and testing"
- **Change type:** Task (Development infrastructure)
- **Change categorized:** Patch (Development process improvement)
- **Impacts:** Improves the process of building and testing Bokeh using Docker.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:**  Changes were made to how Bokeh's Docker images are built and tested, likely to make the process more efficient, reliable, or up-to-date.
- **Code examples:** Not applicable, as this relates to Docker configuration and build scripts.
- **One-sentence summary:** This task updates the Docker image building and testing process for Bokeh development.
</change_breakdown>

<change_number>13</change_number>
<change_description>
This task involves updates to the way Bokeh's Docker images are built and tested. Docker is a platform for developing, shipping, and running applications in containers. These changes likely aim to improve the efficiency, reliability, or maintainability of the Docker-related development workflows.
</change_description>

<code_example>
Not applicable, as this relates to Docker configuration and build scripts, not user-facing code.
</code_example>

<simple_explanation>
Imagine you have a set of instructions for building a robot (Bokeh) using Lego bricks (Docker). This task is like updating those instructions to make the building process faster, easier, and more reliable.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12547 [component: docs] Added metadata to glyphs.py, multi_legend.py, multi_scale.py"
- **Change type:** Task (Documentation improvement)
- **Change categorized:** Patch (Documentation quality)
- **Impacts:** Improves the organization and discoverability of examples by adding metadata.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** Metadata (data about data) was added to specific example files (`glyphs.py`, `multi_legend.py`, `multi_scale.py`) to make them easier to find and understand.
- **Code examples:** Not applicable, as this is a metadata change within example files.
- **One-sentence summary:** This task adds metadata to specific example files to improve their organization and searchability.
</change_breakdown>

<change_number>14</change_number>
<change_description>
This task involves adding metadata to three specific example files: `glyphs.py`, `multi_legend.py`, and `multi_scale.py`. Metadata is data that provides information about other data. In this context, it likely includes information like the example's title, description, tags, or author, which can be used to improve the organization, searchability, and discoverability of the examples.
</change_description>

<code_example>
Not applicable, as this is a metadata change within example files. The metadata itself might look something like this (though the exact format may vary):

```
# .. title: Example of Glyphs
# .. author: Bokeh Team
# .. tags: glyphs, scatter, line
```
</code_example>

<simple_explanation>
Imagine you have a collection of photos (examples). This task is like adding labels and descriptions to each photo so you can easily find them later based on what's in them.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12605 Replace flake8 with ruff"
- **Change type:** Task (Development tooling)
- **Change categorized:** Patch (Development process improvement)
- **Impacts:** Changes the code linting tool used in the project, potentially affecting how code style and quality are enforced.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:**  The project switched from using `flake8` to `ruff` for code linting. Linting tools help enforce coding style guidelines and identify potential errors.
- **Code examples:** Not applicable, as this is a change in development tooling.
- **One-sentence summary:** This task replaces the code linting tool `flake8` with `ruff`.
</change_breakdown>

<change_number>15</change_number>
<change_description>
This task involves switching the code linting tool used in the Bokeh project from `flake8` to `ruff`. Linting tools automatically analyze code for potential errors, style inconsistencies, and other issues. This change likely aims to improve the speed, efficiency, or effectiveness of the linting process.
</change_description>

<code_example>
Not applicable, as this is a change in development tooling, not user-facing code.
</code_example>

<simple_explanation>
Imagine you have a proofreader (linter) who checks your writing for mistakes. This task is like switching to a new, faster proofreader who can catch more errors.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12620 Remove LGTM"
- **Change type:** Task (Development tooling)
- **Change categorized:** Patch (Development process improvement)
- **Impacts:** Removes the LGTM code analysis platform from the project.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** The project stopped using LGTM, a platform for automated code review and analysis.
- **Code examples:** Not applicable.
- **One-sentence summary:** This task removes the LGTM code analysis platform from the project.
</change_breakdown>

<change_number>16</change_number>
<change_description>
This task removes LGTM from the Bokeh project. LGTM is a code analysis platform that helps identify potential bugs and security vulnerabilities. The reasons for removing it could include switching to a different platform, relying on other tools, or changes in project priorities.
</change_description>

<code_example>
Not applicable, as this is a change in development tooling, not user-facing code.
</code_example>

<simple_explanation>
Imagine you have a security guard (LGTM) who checks your building for problems. This task is like deciding you no longer need that specific security guard, perhaps because you have other security measures in place.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12630 Update CodeQL action"
- **Change type:** Task (Development tooling)
- **Change categorized:** Patch (Development process improvement)
- **Impacts:** Updates the CodeQL action used for security analysis, potentially improving the effectiveness of security checks.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** The project updated the CodeQL action, which is used for automated security analysis of the codebase.
- **Code examples:** Not applicable.
- **One-sentence summary:** This task updates the CodeQL action to a newer version for improved security analysis.
</change_breakdown>

<change_number>17</change_number>
<change_description>
This task involves updating the CodeQL action used in the Bokeh project. CodeQL is a security analysis tool that helps identify vulnerabilities in code. Updating the action likely means using a newer version with improved analysis capabilities, bug fixes, or support for new security checks.
</change_description>

<code_example>
Not applicable, as this is a change in development tooling related to GitHub Actions, not user-facing code.
</code_example>

<simple_explanation>
Imagine you have a security system (CodeQL) that scans your house for intruders. This task is like upgrading that system to a newer model that can detect more types of intruders and is more reliable.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12636 Add CodeQL config"
- **Change type:** Task (Development tooling)
- **Change categorized:** Patch (Development process improvement)
- **Impacts:** Adds a configuration for CodeQL, potentially customizing how security analysis is performed.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:**  A configuration file for CodeQL was added, allowing customization of the security analysis process.
- **Code examples:** Not applicable.
- **One-sentence summary:** This task adds a configuration file for CodeQL to customize security analysis.
</change_breakdown>

<change_number>18</change_number>
<change_description>
This task involves adding a configuration file for CodeQL. This allows the Bokeh developers to customize how CodeQL performs its security analysis. The configuration file might specify things like which types of vulnerabilities to scan for, which files or directories to include or exclude, or other settings related to the analysis process.
</change_description>

<code_example>
Not applicable, as this is a configuration change for a development tool, not user-facing code.
</code_example>

<simple_explanation>
Imagine you have a security system (CodeQL) for your house. This task is like adding a control panel that lets you adjust the settings of the system, such as which areas to monitor or what types of alerts to receive.
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12639 Disable docker from wheel integration tests"
- **Change type:** Task (Development process)
- **Change categorized:** Patch (Development process improvement)
- **Impacts:** Modifies the integration testing process by disabling Docker for wheel tests.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** Docker is no longer used in the integration tests that involve building and testing Python wheels (a distribution format).
- **Code examples:** Not applicable.
- **One-sentence summary:** This task disables the use of Docker in wheel integration tests.
</change_breakdown>

<change_number>19</change_number>
<change_description>
This task changes how integration tests are performed for Bokeh, specifically for tests involving Python wheels (a package format). Docker, a containerization platform, is no longer used in these specific tests. The reasons for this change could include simplifying the testing process, avoiding Docker-related issues, or relying on alternative testing methods.
</change_description>

<code_example>
Not applicable, as this is a change to the testing process, not user-facing code.
</code_example>

<simple_explanation>
Imagine you have two ways to test a toy: using a special testing machine (Docker) or testing it by hand. This task is like deciding to only test the toy by hand for certain types of toys (wheels).
</simple_explanation>

<change_breakdown>
- **Change quoted:** "#12645 CodeQL: remove import linter hack"
- **Change type:** Task (Development tooling)
- **Change categorized:** Patch (Development process improvement)
- **Impacts:** Removes a workaround related to import linting in the CodeQL configuration.
- **Backward compatibility:** No user-facing impact.
- **Simple explanations:** A temporary fix or workaround related to import linting within the CodeQL setup was removed, likely because a better solution was found or the issue was resolved.
- **Code examples:** Not applicable.
- **One-sentence summary:** This task removes a temporary "hack" related to import linting in the CodeQL configuration.
</change_breakdown>

<change_number>20</change_number>
<change_description>
This task involves removing a "hack" or workaround that was previously used to address an issue with import linting in the CodeQL configuration. Import linting refers to checking the way Python modules are imported in the code. The hack was likely a temporary solution, and its removal suggests that a proper fix has been implemented or the issue is no longer relevant.
</change_

Okay, let's break down this changelog for Bokeh, starting with version 3.6.

## Bokeh 3.6 Changelog Explanation

### **Bug Fixes**

<change_breakdown>
[ ] Change quoted: "#4951 ModelExtensions - all resources from a whole module are loaded"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects loading of custom models (extensions). Ensures all necessary resources are available.
[ ] Backward compatibility considered: Fixes an issue where extensions might not have functioned correctly. No backward compatibility issues expected.
[ ] Simple explanations brainstormed:
    *  Previously, some parts of custom models might have been missing. Now, everything is loaded properly.
    *  Think of it like ordering a meal and not getting all the sides. Now you get the whole meal.
[ ] Code examples outlined:
    *  Difficult to demonstrate without a specific custom model example. The issue was related to internal resource loading.
[ ] One-sentence summary written: This fixes an issue where custom model extensions might have been missing resources, ensuring they are now loaded completely.
</change_breakdown>

<change_number>1</change_number>
<change_description>
This change addresses a problem where custom model extensions in Bokeh might not have been loading all their required resources. Custom models, or extensions, allow users to extend Bokeh's functionality beyond its built-in features. This bug fix ensures that when an extension is used, all the necessary JavaScript, CSS, and other resources from the extension's module are loaded correctly, guaranteeing that the extension works as intended.
</change_description>

<code_example>
```python
# This is a conceptual example. The actual fix is in the internal loading mechanism.

# Hypothetical custom model (before fix)
# class MyCustomModel(Model):
#     __implementation__ = "my_custom_model.ts" # MyCustomModel may have lacked resources

# Hypothetical custom model (after fix)
# class MyCustomModel(Model):
#     __implementation__ = "my_custom_model.ts" # Resources are loaded correctly

# No code changes are required for users to benefit from this fix.
```
</code_example>

<simple_explanation>
Imagine you bought a build-it-yourself furniture kit, but some parts were missing. This fix is like making sure all the parts are now included in the kit, so you can build your furniture correctly. If you were using custom model extensions in Bokeh, they might not have worked perfectly before. Now, they should work as expected because all the necessary pieces are loaded.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#7524 GroupFilter only accepts strings"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects `GroupFilter`. Now it can accept other data types besides strings, making it more flexible.
[ ] Backward compatibility considered: No backward compatibility issues, as it expands functionality.
[ ] Simple explanations brainstormed:
    *  `GroupFilter` was like a bouncer that only let people with string names into the club. Now it accepts other types too.
    *  It used to be picky about data types, now it's more inclusive.
[ ] Code examples outlined:
    *  Demonstrate using `GroupFilter` with numbers before and after the fix.
[ ] One-sentence summary written: `GroupFilter` now works with various data types, not just strings, increasing its flexibility.
</change_breakdown>

<change_number>2</change_number>
<change_description>
This change fixes a limitation in Bokeh's `GroupFilter`, which is used to filter data based on group membership. Previously, `GroupFilter` could only handle string values for group names. This update allows it to work with other data types like numbers, making it more versatile for filtering data in various scenarios.
</change_description>

<code_example>
```python
from bokeh.models import ColumnDataSource, GroupFilter, CDSView
from bokeh.plotting import figure, show

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y=[2, 5, 8, 2, 7],
    group=['A', 'B', 1, 'A', 2]  # Group now includes numbers
))

# Before the fix, this would likely not work as expected
view = CDSView(source=source, filters=[GroupFilter(column_name='group', group=1)])

p = figure(width=400, height=400)
p.circle('x', 'y', size=20, source=source, view=view)

show(p)
```
</code_example>

<simple_explanation>
Think of `GroupFilter` as a way to sort your toys into different boxes. Before, you could only sort toys into boxes labeled with words (strings). Now, you can also sort them into boxes labeled with numbers or other types of labels. This makes it easier to organize your data in more ways.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#13827 [component: bokehjs] [BUG] Lack of range expansion when there remains unbounded directions, even when `maintain_focus=False`"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects BokehJS plotting when `maintain_focus=False`. Ranges will now expand correctly in all directions.
[ ] Backward compatibility considered: Fixes incorrect behavior. No backward compatibility issues.
[ ] Simple explanations brainstormed:
    *  Previously, plots might not have zoomed out properly in all directions. Now they do.
    *  Like a camera that could only zoom in, now it can zoom in and out correctly.
[ ] Code examples outlined:
    *  Difficult to demonstrate without a complex plotting scenario. The issue was related to range calculation logic.
[ ] One-sentence summary written: This fixes an issue where plots wouldn't adjust their zoom/range correctly in certain situations, making them behave more predictably.
</change_breakdown>

<change_number>3</change_number>
<change_description>
This bug fix addresses an issue in BokehJS related to how plot ranges (the visible area of the plot) are adjusted when the `maintain_focus` option is set to `False`. In certain scenarios, the plot range wouldn't expand correctly when there were "unbounded directions," meaning there was no data limiting the view in that direction. This fix ensures that ranges expand properly in all directions, even when `maintain_focus` is `False`, providing a more consistent and expected behavior when interacting with plots.
</change_description>

<code_example>
```javascript
// Conceptual example (JavaScript/BokehJS)

// Before the fix, in some cases with maintain_focus=false, the plot range 
// might not have expanded correctly if there were unbounded directions.

// After the fix, the range expands correctly.

// No specific code change is needed from the user's side to benefit from this fix.
// It's an internal improvement in how BokehJS calculates ranges.
```
</code_example>

<simple_explanation>
Imagine you have a map that you can zoom in and out of. Sometimes, when you tried to zoom out to see more of the map, it wouldn't show you everything. This fix is like making the map work correctly, so you can always zoom out and see the whole area you want to see.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#13886 [component: bokehjs] [BUG] NPM package has types (*.d.ts) in incorrect location"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects TypeScript users of BokehJS via NPM. Type definitions are now in the correct location, improving development experience.
[ ] Backward compatibility considered: No backward compatibility issues. Only affects development.
[ ] Simple explanations brainstormed:
    *  Type definitions are like instruction manuals for code. They were in the wrong place, making it hard for TypeScript to understand BokehJS. Now they're in the right place.
    *  It's like having a library with books in the wrong sections. Now they're organized correctly.
[ ] Code examples outlined:
    *  Not applicable, as this is a build/packaging issue, not a code issue.
[ ] One-sentence summary written: This fixes the location of TypeScript type definitions in the BokehJS NPM package, making it easier for TypeScript developers to use BokehJS.
</change_breakdown>

<change_number>4</change_number>
<change_description>
This is a bug fix specifically for developers using BokehJS with TypeScript through the NPM package manager. TypeScript relies on type definition files (`*.d.ts`) to understand the structure and types used in JavaScript libraries like BokehJS. This fix corrects the location of these type definition files within the NPM package. Previously, they were in the wrong place, which could cause issues for TypeScript users. Now, they are in the correct location, making it easier to integrate BokehJS into TypeScript projects.
</change_description>

<code_example>
```
// Not applicable. This is a fix related to the packaging of BokehJS for NPM,
// not a code change that users would make.
```
</code_example>

<simple_explanation>
Imagine you have a cookbook (your code) that needs instructions (type definitions) to use ingredients from a specific brand (BokehJS). Before, the instructions were in the wrong cookbook or a different section. This fix puts the instructions in the right place, so your cookbook can understand how to use the ingredients correctly. If you're using TypeScript with BokehJS, this makes your development process smoother.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#13957 [component: bokehjs] Explicit selection glyph example broken"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects examples demonstrating explicit selection glyphs. They are now fixed and work correctly.
[ ] Backward compatibility considered: No backward compatibility issues. Only affects examples.
[ ] Simple explanations brainstormed:
    *  Some examples showcasing a specific feature were broken. Now they work.
    *  Like a tutorial with incorrect steps, now the steps are correct.
[ ] Code examples outlined:
    *  Refer to the updated example in the Bokeh documentation or repository.
[ ] One-sentence summary written: The example demonstrating explicit selection glyphs in BokehJS was broken and has been fixed.
</change_breakdown>

<change_number>5</change_number>
<change_description>
This change fixes a broken example in the Bokeh documentation or examples repository related to "explicit selection glyphs." Selection glyphs are visual representations of selected data points in a plot. "Explicit" likely refers to a specific way of defining or customizing these glyphs. The example was likely not functioning correctly, and this fix ensures that it now works as intended, providing a working demonstration of how to use explicit selection glyphs.
</change_description>

<code_example>
```
# Refer to the updated example in the Bokeh documentation or repository
# for the correct code demonstrating explicit selection glyphs.

# The specific code that was broken and fixed is not detailed in the changelog,
# but the updated example will showcase the correct implementation.
```
</code_example>

<simple_explanation>
Think of this like a recipe in a cookbook that had incorrect instructions. Because of this, when you followed the recipe, the dish didn't turn out right. This fix is like correcting the instructions in the recipe, so now if you follow them, the dish will be made correctly. In this case, the "dish" is an example showing how to use a specific feature of Bokeh, and the "recipe" is the example code.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#13959 [BUG] Reset Tool Error in Bokeh Gridplot with Single Plot"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects `ResetTool` when used with a single plot in a `GridPlot`. It now works without errors.
[ ] Backward compatibility considered: No backward compatibility issues. Fixes incorrect behavior.
[ ] Simple explanations brainstormed:
    *  The `ResetTool`, which resets a plot to its original view, was causing an error when used with a single plot in a grid layout. Now it works correctly.
    *  Like a "reset" button that was broken in a specific situation, now it works as expected.
[ ] Code examples outlined:
    *  Demonstrate creating a `GridPlot` with a single plot and using `ResetTool`.
[ ] One-sentence summary written: The `ResetTool` now functions correctly when used with a single plot in a `GridPlot`, preventing errors that occurred before.
</change_breakdown>

<change_number>6</change_number>
<change_description>
This change fixes a bug that caused an error when using the `ResetTool` with a `GridPlot` containing only a single plot. The `ResetTool` is a tool that allows users to reset the view of a plot back to its original state (e.g., after zooming or panning). `GridPlot` is a layout that arranges multiple plots in a grid. This fix ensures that the `ResetTool` now works correctly in this specific scenario, preventing the error that occurred previously.
</change_description>

<code_example>
```python
from bokeh.plotting import figure, show
from bokeh.models import GridPlot, ResetTool

# Create a single plot
p = figure(width=300, height=300, tools=[ResetTool()])
p.circle([1, 2, 3], [4, 5, 6])

# Create a GridPlot with the single plot
grid = GridPlot(children=[[p]], width=300, height=300)

# Before the fix, adding a ResetTool to a GridPlot with a single plot might have caused an error.
# Now it works correctly.

show(grid)
```
</code_example>

<simple_explanation>
Imagine you have a picture frame (GridPlot) where you can put photos (plots). You also have a magic button (ResetTool) that can put the photo back in its original position if you move it. Before, if you only had one photo in the frame and used the magic button, it would mess things up. This fix makes sure the magic button works properly even if there's only one photo in the frame.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#13964 [component: bokehjs] [BUG] page won't render if CustomJS args has a dict with key \"constructor\""
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects `CustomJS` when used with a dictionary containing the key "constructor". This is now handled correctly, preventing rendering issues.
[ ] Backward compatibility considered: Fixes incorrect behavior. No backward compatibility issues.
[ ] Simple explanations brainstormed:
    *  `CustomJS` lets you add custom JavaScript code to your Bokeh plots. If you used a dictionary with the word "constructor" as a key, it would break the page. Now it works.
    *  Like a specific word that was causing a computer program to crash, now the program can handle that word without issues.
[ ] Code examples outlined:
    *  Demonstrate using `CustomJS` with a dictionary containing the key "constructor".
[ ] One-sentence summary written: Bokeh pages will no longer fail to render if a `CustomJS` callback uses a dictionary argument that contains the key "constructor".
</change_breakdown>

<change_number>7</change_number>
<change_description>
This bug fix addresses an issue in BokehJS where a web page would fail to render if a `CustomJS` callback used a dictionary that contained the key "constructor" in its arguments. `CustomJS` allows users to define custom JavaScript code that can interact with Bokeh objects. This bug was likely due to a conflict with the special meaning of "constructor" in JavaScript. The fix ensures that BokehJS now correctly handles dictionaries containing the "constructor" key, preventing the rendering failure.
</change_description>

<code_example>
```python
from bokeh.models import CustomJS, Slider
from bokeh.plotting import figure, show
from bokeh.layouts import column

# Create a plot
p = figure(width=400, height=400)
p.circle([1, 2, 3], [4, 5, 6])

# Before the fix, this CustomJS code might have caused the page to not render
# because of the "constructor" key.
callback = CustomJS(args=dict(my_dict={"constructor": "some_value"}), code="""
    console.log(my_dict);
""")

slider = Slider(start=0, end=10, value=1, step=0.1, title="Slider")
slider.js_on_change('value', callback)

show(column(slider, p))
```
</code_example>

<simple_explanation>
Imagine you have a robot (Bokeh) that you can give instructions to using special cards (CustomJS). One of the cards has the word "constructor" written on it. Before, if you used this card in a specific way, the robot would get confused and stop working. This fix is like teaching the robot how to understand that card correctly, so it doesn't get confused anymore. Now you can use the "constructor" card without breaking the robot.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#13965 [component: bokehjs] [BUG] CategoricalSlider shows ‘undefined’ value and skip that value"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects `CategoricalSlider`. It now correctly displays and handles all values, including those that might have appeared as 'undefined'.
[ ] Backward compatibility considered: Fixes incorrect behavior. No backward compatibility issues.
[ ] Simple explanations brainstormed:
    *  `CategoricalSlider` was showing 'undefined' for some values and skipping them. Now it shows and handles all values correctly.
    *  Like a slider that was missing some numbers on it, now all the numbers are there and it works smoothly.
[ ] Code examples outlined:
    *  Demonstrate using `CategoricalSlider` with values that might have previously shown as 'undefined'.
[ ] One-sentence summary written: The `CategoricalSlider` now correctly displays and handles all its values, fixing an issue where some values might have been displayed as 'undefined' and skipped.
</change_breakdown>

<change_number>8</change_number>
<change_description>
This change fixes a bug in the `CategoricalSlider` widget where some values might have been displayed as 'undefined' and skipped over when using the slider. The `CategoricalSlider` is a widget that allows users to select a value from a predefined set of categories (e.g., "apple", "banana", "orange"). This fix ensures that all categories are displayed correctly and that the slider doesn't skip any values.
</change_description>

<code_example>
```python
from bokeh.models import CategoricalSlider
from bokeh.plotting import show
from bokeh.layouts import column

# Before the fix, some values might have shown as 'undefined' and been skipped.
slider = CategoricalSlider(title="Select a fruit", options=["apple", "banana", "orange", None])

# Now all values are displayed and handled correctly.

show(column(slider))
```
</code_example>

<simple_explanation>
Imagine you have a toy with buttons for different colors (CategoricalSlider). Before, some buttons might have shown the word "undefined" instead of the color name, and pressing them wouldn't do anything. This fix is like relabeling those buttons with the correct color names and making them work properly. Now all the buttons show the right colors, and you can select any of them.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#13972 BOKEH_MINIFIED not working"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects the `BOKEH_MINIFIED` environment variable. It now correctly controls whether minified JavaScript is used.
[ ] Backward compatibility considered: Fixes incorrect behavior. No backward compatibility issues.
[ ] Simple explanations brainstormed:
    *  `BOKEH_MINIFIED` is a setting that controls whether a smaller, faster version of BokehJS is used. It wasn't working properly, but now it does.
    *  Like a switch that was supposed to turn on the lights but didn't, now the switch works.
[ ] Code examples outlined:
    *  Not applicable, as this is an environment variable issue, not a code issue.
[ ] One-sentence summary written: The `BOKEH_MINIFIED` environment variable now correctly controls the use of minified BokehJS resources.
</change_breakdown>

<change_number>9</change_number>
<change_description>
This change fixes an issue with the `BOKEH_MINIFIED` environment variable. This variable is used to control whether Bokeh uses the minified (compressed for faster loading) version of its JavaScript files. Minified files are smaller and load faster, but they are harder to read and debug. This fix ensures that the `BOKEH_MINIFIED` variable now correctly toggles between the minified and non-minified versions of BokehJS.
</change_description>

<code_example>
```
# Not applicable. This fix is related to how Bokeh handles the BOKEH_MINIFIED
# environment variable, not a code change that users would make.

# To use the minified version (typically for production):
# BOKEH_MINIFIED=true bokeh serve my_app.py

# To use the non-minified version (typically for development/debugging):
# BOKEH_MINIFIED=false bokeh serve my_app.py
```
</code_example>

<simple_explanation>
Imagine you have two versions of a map: a big, detailed one (non-minified) and a smaller, simplified one (minified). You have a switch (BOKEH_MINIFIED) that lets you choose which map to use. Before, the switch was broken, and you couldn't always get the map you wanted. This fix is like repairing the switch so you can now choose between the detailed map for exploring or the smaller map for quick reference.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#13984 [component: tests] [BUG] Deprecation warning treated as error in pytest hook"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects testing with pytest. Deprecation warnings no longer cause test failures.
[ ] Backward compatibility considered: No backward compatibility issues. Only affects testing.
[ ] Simple explanations brainstormed:
    *  Deprecation warnings are like "heads up" messages about things that might change in the future. They were causing tests to fail, but now they don't.
    *  Like a smoke alarm that was too sensitive, now it only goes off for actual fires.
[ ] Code examples outlined:
    *  Not applicable, as this is a testing configuration issue, not a code issue.
[ ] One-sentence summary written: This fixes an issue in testing where deprecation warnings were incorrectly treated as errors, preventing tests from passing unnecessarily.
</change_breakdown>

<change_number>10</change_number>
<change_description>
This change is a bug fix related to testing Bokeh code with the pytest framework. Previously, deprecation warnings (messages indicating that some code might be removed or changed in the future) were being treated as errors by a pytest hook. This caused tests to fail even if the code being tested was working correctly. This fix adjusts the pytest hook so that deprecation warnings are no longer treated as errors, allowing tests to pass as long as there are no actual errors.
</change_description>

<code_example>
```
# Not applicable. This is a fix related to how Bokeh's tests are run with pytest,
# not a code change that users would make in their own code.
```
</code_example>

<simple_explanation>
Imagine you're taking a test (running tests on your code), and the teacher (pytest) tells you that some questions might be removed from the test next year (deprecation warning). Before, the teacher would mark your whole test wrong just because of this warning, even if you answered all the current questions correctly. This fix is like the teacher now understanding that the warning is just a heads-up for the future and not a reason to fail the current test.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#14014 [component: bokehjs] [BUG] StringFormatter `nan_format` seems broken"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects `StringFormatter`, specifically how it handles NaN (Not a Number) values. It now formats them correctly according to the `nan_format` setting.
[ ] Backward compatibility considered: Fixes incorrect behavior. No backward compatibility issues.
[ ] Simple explanations brainstormed:
    *  `StringFormatter` is used to format numbers as strings. It wasn't handling NaN values correctly, but now it does.
    *  Like a number formatting tool that was displaying "???" for invalid numbers, now it shows what you want it to show (e.g., "N/A").
[ ] Code examples outlined:
    *  Demonstrate using `StringFormatter` with a `DataTable` and setting `nan_format`.
[ ] One-sentence summary written: The `StringFormatter` now correctly formats NaN values according to the specified `nan_format`.
</change_breakdown>

<change_number>11</change_number>
<change_description>
This change fixes a bug in Bokeh's `StringFormatter` where the `nan_format` option was not working correctly. `StringFormatter` is used to format numerical values as strings, for example, in tables or tooltips. The `nan_format` option allows you to specify how "Not a Number" (NaN) values should be displayed. This fix ensures that NaN values are now formatted according to the `nan_format` setting.
</change_description>

<code_example>
```python
from bokeh.models import ColumnDataSource, DataTable, TableColumn, NumberFormatter, StringFormatter
from bokeh.plotting import show
import numpy as np

data = {'values': [1.23, 4.56, float('nan'), 7.89]}
source = ColumnDataSource(data)

columns = [
    TableColumn(field="values", title="Values", formatter=NumberFormatter()),
    TableColumn(field="values", title="Values (formatted)", 
                formatter=StringFormatter(nan_format='-')), # Use StringFormatter and specify nan_format
]

data_table = DataTable(source=source, columns=columns, width=400, height=280)

# Before the fix, the nan_format might not have been applied correctly.
# Now, NaN values will be displayed as '-' in the second column.

show(data_table)
```
</code_example>

<simple_explanation>
Imagine you have a label maker (StringFormatter) that you use to print labels for your items. You have some items that don't have a proper value (NaN), and you want to label them as "Unknown" (nan_format). Before, the label maker was ignoring your instruction and just printing a blank label for those items. This fix is like fixing the label maker so it now prints "Unknown" on the labels for those items, just like you wanted.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#14054 [component: bokehjs] [BUG] Custom hover tooltip on image plot shows all the image data."
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects custom hover tooltips on image plots. They now display the correct information instead of the entire image data.
[ ] Backward compatibility considered: Fixes incorrect behavior. No backward compatibility issues.
[ ] Simple explanations brainstormed:
    *  Hover tooltips on image plots were showing too much information. Now they show only the relevant data.
    *  Like a magnifying glass that was showing you the whole page instead of just the zoomed-in part, now it shows only the part you're looking at.
[ ] Code examples outlined:
    *  Difficult to demonstrate without a complex image plot example. The issue was related to how hover tooltips were constructed for images.
[ ] One-sentence summary written: Custom hover tooltips on image plots now display the correct, concise information instead of the entire image data.
</change_breakdown>

<change_number>12</change_number>
<change_description>
This bug fix addresses an issue with custom hover tooltips on image plots in BokehJS. Previously, when you hovered over an image plot with a custom tooltip, the tooltip might have displayed the entire image data instead of the specific information you wanted to show for the hovered point. This fix ensures that the tooltip now displays only the relevant information, making it much more useful for exploring image data.
</change_description>

<code_example>
```python
# Conceptual example (the actual fix is in how BokehJS handles hover tooltips for images)

# Before the fix, a custom tooltip on an image plot might have shown the entire image data.

# After the fix, it shows only the relevant information for the hovered point.

# No specific code change is needed from the user's side to benefit from this fix.
# It's an internal improvement in how BokehJS constructs tooltips for images.
```
</code_example>

<simple_explanation>
Imagine you have a special photo album (image plot) where you can point at a photo (hover) and see a note (tooltip) about it. Before, when you pointed at a photo, the note would show you all the details about every photo in the album, which was overwhelming! This fix is like making the notes more focused, so now when you point at a photo, the note only tells you about that specific photo, which is much more helpful.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#14058 [component: bokehjs] [BUG] Clearing selection with ESC only works on first selection tool"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects clearing selections with the ESC key. It now works consistently across all selection tools.
[ ] Backward compatibility considered: Fixes incorrect behavior. No backward compatibility issues.
[ ] Simple explanations brainstormed:
    *  Pressing ESC to clear a selection was only working for the first selection tool you used. Now it works for all of them.
    *  Like an "undo" button that only worked once, now it works multiple times for different actions.
[ ] Code examples outlined:
    *  Difficult to demonstrate without a complex plot with multiple selection tools.
[ ] One-sentence summary written: The ESC key now consistently clears selections across all selection tools in BokehJS.
</change_breakdown>

<change_number>13</change_number>
<change_description>
This change fixes a bug in BokehJS where pressing the ESC key to clear a selection would only work for the first selection tool that was used. Bokeh has various selection tools (e.g., box select, lasso select) that allow users to select data points on a plot. This fix ensures that the ESC key now works consistently across all selection tools, allowing users to clear selections reliably regardless of which tool was used.
</change_description>

<code_example>
```javascript
// Conceptual example (JavaScript/BokehJS)

// Before the fix, pressing ESC might only have cleared the selection 
// for the first selection tool that was used.

// After the fix, pressing ESC clears the selection for any active selection tool.

// No specific code change is needed from the user's side to benefit from this fix.
// It's an internal improvement in how BokehJS handles keyboard events.
```
</code_example>

<simple_explanation>
Imagine you have a drawing program (Bokeh) where you can select different shapes (data points) using different tools (selection tools). You also have an eraser button (ESC key) to unselect shapes. Before, the eraser button would only work for the first tool you used. If you switched to a different tool, the eraser wouldn't work anymore. This fix is like making the eraser button work for all the tools, so you can always unselect shapes no matter which tool you're using.
</simple_explanation>
<br>

<change_breakdown>
[ ] Change quoted: "#14068 [component: bokehjs] [BUG] Unable to change figures displayed by altering children attribute of gridplot (or other layout classes) in JS callback"
[ ] Change type identified: Bug fix
[ ] Change categorized: Minor
[ ] Impacts listed: Affects dynamically updating `GridPlot` (or other layouts) in JavaScript callbacks. It's now possible to change the displayed figures by modifying the `children` attribute.
[ ] Backward compatibility considered: Fixes incorrect behavior. No backward compatibility issues.
[ ] Simple explanations brainstormed:
    *  You couldn't change the plots inside a `GridPlot` using JavaScript callbacks before. Now you can.
    *  Like a photo album where you couldn't swap out photos using a remote control, now you can.
[ ] Code examples outlined:
    *  Demonstrate updating a `GridPlot`'s `children` in a `CustomJS` callback.
[ ] One-sentence summary written: It's now possible to dynamically update the figures displayed in a `GridPlot` (or other layout) by modifying its `children` attribute within a JavaScript callback.
</change_breakdown>

<change_number>14</change_number>
<change_description>
This bug fix addresses an issue in BokehJS where it was not possible to change the figures displayed within a `GridPlot` (or other layout classes like `Column` or `Row`) by modifying the `children` attribute in a JavaScript callback. This fix enables dynamic updating of layouts, allowing developers to create more interactive and responsive visualizations.
</change_description>

<code_example>
```python
from bokeh.layouts import column, gridplot
from bokeh.models import Button, CustomJS
from bokeh.plotting import figure, show

# Initial plots
p1 = figure(width=200, height=200)
p1.circle([1, 2], [3, 4])
p2 = figure(width=200, height=200)
p2.line([1, 2], [3, 4])

# Create a GridPlot
grid = gridplot([[p1, p2]], width=200, height=200)

# New plots to be displayed
p3 = figure(width=200, height=200)
p3.square([1, 2], [3, 4])
p4 = figure(width=200, height=200)
p4.diamond([1, 2], [3, 4])

# CustomJS callback to update the GridPlot
callback = CustomJS(args=dict(grid=grid, p3=p3, p4=p4), code="""
    grid.children = [[p3, p4]];
""")

button = Button(label="Update Grid", callback=callback)

# Before the fix, this wouldn't have updated the GridPlot.
# Now it dynamically changes the displayed plots.

show(column(button, grid))
```
</code_example>

<simple_explanation>
Imagine you have a digital picture frame (GridPlot) that can display multiple pictures (plots). You also have a remote control (JavaScript callback) that you can use to change the pictures. Before, the remote control couldn't change the pictures in the frame. This fix

