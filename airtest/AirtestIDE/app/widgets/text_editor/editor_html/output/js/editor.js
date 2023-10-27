function confirmDialog(e,t,i,n){e.openConfirm?e.openConfirm(t,n):confirm(i)&&n[0]()}var editor=CodeMirror(document.body),imgMarkerList=[],doReplaceConfirm="<div class='confirmInsertDiv'> Poco mode has changed. Do you want to insert poco init code at the current cursor position? <a class='dialogBtn'>Yes</a> <a class='dialogBtn'>No</a> </div>";$(function(){function e(e,t){if(!editor.state.completionActive&&13!=t.keyCode&&27!=t.keyCode){editor.removeLineError();var i=editor.getCursor(),n=e.getDoc().getLine(i.line),o=/((touch|swipe)\(Template\(.*\)\))(,\s*.*)*\)/g,r=o.exec(n);if(r&&r[2])i.ch>r.index+r[1].length&&i.ch<r.index+r[0].length&&e.showHint({hint:CodeMirror.hint.airtest,completeSingle:!1});else{var d=editor.getTokenAt(i),a="";d.string.match(/^[.`\w@]\w*$/)&&(a=d.string),a.length>0&&e.showHint("0"!=qtbridge.enableAutoComplete?{hint:CodeMirror.hint.jedi,completeSingle:!1}:{hint:CodeMirror.hint.poco,completeSingle:!1})}}}function t(e,t,i){var n=editor.doc.markText(e,t,{className:"imgEditor",replacedWith:i,readonly:!0});imgMarkerList.push(n)}CodeMirror.registerHelper("hint","python",CodeMirror.pythonHint);var i,n=200;editor.on("keyup",function(t,o){clearTimeout(i),i=setTimeout(function(){e(t,o)},n)}),editor.removeLineError=function(){globalVariable.running_failed&&(editor.getDoc().removeLineClass(globalVariable.active_line,"background","line-error-MoonLight"),editor.getDoc().removeLineClass(globalVariable.active_line,"background","line-error-DarkShadow"),globalVariable.running_failed=!1)},editor.removeLineRunning=function(){editor.getDoc().removeLineClass(globalVariable.active_line,"background","line-running-MoonLight"),editor.getDoc().removeLineClass(globalVariable.active_line,"background","line-running-DarkShadow")},editor.addText=function(e,t,i){editor.removeLineError(),t&&(e+="\n"),i||(i=editor.getCursor()),editor.doc.replaceRange(e,i,i),t?editor.setCursor({line:i.line+e.split(/\r\n|\r|\n/).length-1,ch:0}):(editor.setCursor({line:i.line+e.split(/\r\n|\r|\n/).length-1,ch:0}),editor.execCommand("goLineEnd")),editor.focus()},editor.smartAddText=function(e,t,i,n){if(t="undefined"!=typeof t?t:!0,n="undefined"!=typeof n?n:!1,editorText=editor.getDoc().getValue(),!editorText.includes(e)||n)if(editor.removeLineError(),t&&(e+="\n"),editorText.includes(i)){pos=0,lines=editor.doc.eachLine(function(e){editor.doc.lineInfo(e).text.includes(i)&&(pos={line:editor.doc.lineInfo(e).line+1,ch:0})}),newContent="\n"+e,editor.doc.replaceRange(newContent,pos,pos);var o=pos.line;t?editor.setCursor({line:pos.line+e.split(/\r\n|\r|\n/).length,ch:0}):(editor.setCursor({line:pos.line+e.split(/\r\n|\r|\n/).length-1,ch:0}),editor.execCommand("goLineEnd")),editor.scrollIntoView({line:o,ch:0}),editor.focus()}else editor.addText(e,t,null)},editor.addTextWithImage=function(e,i,n){var o=editor.getCursor();editor.addText(e,i,n);for(var r=/Template\(([\u4e00-\u9fa5\w\s\+\:\/\\\._-]*\.png)(.*?[\)|\]]){0,1}\)/g,d=r.exec(e),a=new Array;null!==d&&d.length>1;){var l=document.createElement("img");l.setAttribute("class","imgClass"),a.push(l),l.setAttribute("src",d[1]),l.setAttribute("alt",d[1]),l.setAttribute("title",d[1]);var c=editor.findPosH(o,d.index,"char"),s=d[0].length,g=editor.findPosH(c,s,"char");!function(e,i,n){setTimeout(function(){t(e,i,n)},1)}(c,g,l),d=r.exec(e)}},editor.addTextWithImageTest=function(e,i,n){var o=editor.getCursor();editor.addText(e,n,null);for(var r=0;r<i.length;r++){var d=editor.findPosH(o,i[r][1][0],"char"),a=editor.findPosH(o,i[r][1][1],"char"),l=document.createElement("img");l.setAttribute("class","imgClass"),l.setAttribute("src",i[r][0]),l.setAttribute("alt",i[r][0]),l.setAttribute("title",i[r][0]),l.setAttribute("data-start",d),l.setAttribute("data-end",a),function(e,i,n){setTimeout(function(){t(e,i,n)},1)}(d,a,l)}},editor.addTextWithLink=function(e,t,i){var n=editor.getCursor();editor.addText(e,t,i);for(var o=/\[([\u4e00-\u9fa5\w\s]*)\]\((http.*)\)/g,r=o.exec(e);null!==r&&r.length>1;){var d=document.createElement("a"),a=document.createTextNode(r[1]);d.setAttribute("href",r[2]),d.setAttribute("class","helpinfo"),d.appendChild(a),d.onclick=function(){return event.preventDefault(),qtbridge.openLink($(this).attr("href")),!1};var l=editor.findPosH(n,r.index,"char"),c=r[0].length,s=editor.findPosH(l,c,"char");editor.doc.markText(l,s,{className:"link",replacedWith:d}),r=o.exec(e)}},editor.on("copy",function(e){var t=e.getSelection();-1!==t.indexOf("Template")&&qtbridge.copy(t)}),editor.on("paste",function(e,t){var i=t.clipboardData.getData("Text");-1!==i.indexOf("Template")&&(t.preventDefault(),qtbridge.paste(i))}),editor.on("change",function(e){var t=e.getDoc().getValue();qtbridge.content=t}),editor.addKeyMap({Tab:function(e){if(e.somethingSelected()){var t=editor.getSelection("\n");if(t.length>0&&(t.indexOf("\n")>-1||t.length===e.getLine(e.getCursor().line).length))return void e.indentSelection("add")}e.execCommand(e.options.indentWithTabs?"insertTab":"insertSoftTab")},"Shift-Tab":function(e){e.indentSelection("subtract")},"Ctrl-/":function(e){e.execCommand("toggleComment")},"Cmd-/":function(e){e.execCommand("toggleComment")}}),CodeMirror.defineSimpleMode("consolelog",{start:[{regex:/\[\w+\]|\<\w+\>/,token:"type"},{regex:/"(?:[^\\]|\\.)*?(?:"|$)/,token:"string"},{regex:/\[(\d|\:)+\]/,token:"variable-2"},{regex:/(?:Traceback|(\w+)Error)\b/,token:"error"},{regex:/\b(?:def|var|return|if|for|while|else|do|this|python|exec|not)\b/,token:"keyword"},{regex:/0x[a-f\d]+|[-+]?(?:\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/i,token:"number"},{regex:/>>>/,token:"atom"},{regex:/\sin\b/,token:"keyword"},{regex:/\s*\w+\s+(?=\:)/,token:"keyword"},{regex:/[\u4e00-\u9fa5]+(?=\:)/,token:"variable-3"}]}),"undefined"!=typeof qt&&new QWebChannel(qt.webChannelTransport,function(e){window.qtbridge=e.objects.qtbridge,init_editor_options(editor,qtbridge.mode,qtbridge.menuLang);var t=qtbridge.fontSize;$("body").css("fontSize",t),editor.refresh(),init_editor_bridge(qtbridge.mode),qtbridge.registrationFinished()}),editor.on("dblclick",function(e,t){if(t.target){var i=$(t.target);if("imgClass"===i.attr("class")){for(var n=e.coordsChar({left:t.clientX,top:t.clientY}),o=e.getLine(n.line),r={line:n.line,ch:0},d={line:n.line,ch:o.length},a=imgMarkerList.filter(function(e){return e.replacedWith==i.context}),l=0;l<a.length;l++){var c=a[l].find();if(c.from.line==n.line&&c.from.ch<=n.ch&&c.to.line==n.line&&c.to.ch>=n.ch)return o=editor.getRange(c.from,c.to),void qtbridge.modify_img(o,c.from,c.to)}qtbridge.modify_img(o,r,d)}}})});