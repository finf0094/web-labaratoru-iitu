-- Personalises the PW6 report from student.json values passed as metadata
-- (student_name, student_group):
--  * replaces the placeholders Name_Surname and GroupNumber everywhere in the text;
--  * renders the ::: {.watermark} div as a small Word text box with the student's name.
local name, group = "Name_Surname", "GroupNumber"

local function personalise(s)
  return (s:gsub("Name_Surname", name):gsub("GroupNumber", group))
end

local function textbox(text)
  return pandoc.RawBlock("openxml", string.format([[
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:pict>
<v:shapetype id="_x0000_t202" coordsize="21600,21600" o:spt="202" path="m,l,21600r21600,l21600,xe">
<v:stroke joinstyle="miter"/><v:path gradientshapeok="t" o:connecttype="rect"/></v:shapetype>
<v:shape id="watermark" type="#_x0000_t202" style="width:170pt;height:22pt" strokecolor="#BFBFBF" strokeweight="0.5pt">
<v:textbox inset="2pt,2pt,2pt,2pt"><w:txbxContent>
<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:color w:val="A6A6A6"/><w:sz w:val="16"/></w:rPr>
<w:t>%s</w:t></w:r></w:p></w:txbxContent></v:textbox></v:shape></w:pict></w:r></w:p>]], text))
end

return {
  {
    Meta = function(meta)
      if meta.student_name then name = pandoc.utils.stringify(meta.student_name) end
      if meta.student_group then group = pandoc.utils.stringify(meta.student_group) end
      return meta
    end,
  },
  {
    Str = function(el) el.text = personalise(el.text); return el end,
    Code = function(el) el.text = personalise(el.text); return el end,
    Div = function(el)
      if el.classes:includes("watermark") then return textbox(name) end
    end,
  },
}
