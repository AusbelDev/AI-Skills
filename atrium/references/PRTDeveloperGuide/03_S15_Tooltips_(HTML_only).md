## Tooltips (HTML only)


Tooltips can be added to a report component (box), to be displayed when hovering the cursor
mouse pointer) over the component. Example:

```
col = p.Column()
col.add(p.Image("logosmall.jpg", align=p.RIGHT,
                 tooltip="I'm an image tooltip!"))
```