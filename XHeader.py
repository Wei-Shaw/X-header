import sublime, sublime_plugin, datetime
 
class XheaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        
        cur_syntax = self.view.settings().get('syntax').lower()
        if cur_syntax.find('php') != -1 :
            tpl_dir = __file__.replace('XHeader.py', 'tpl/php.tpl')
        elif cur_syntax.find('javascript') != -1 :
            tpl_dir = __file__.replace('XHeader.py', 'tpl/js.tpl')
        elif cur_syntax.find('css') != -1 :
            tpl_dir = __file__.replace('XHeader.py', 'tpl/css.tpl')
        else :
            return
        with open(tpl_dir, 'r') as file_object:
            contents = file_object.read()
        settings = sublime.load_settings("XHeader.sublime-settings")
        contents = contents.replace('{{created}}', settings.get('createBy'));
        contents = contents.replace('{{author}}', settings.get('author'));
        contents = contents.replace('{{date}}', datetime.datetime.now().strftime("%Y-%m-%d %H:%M"));
        contents = contents.replace('{{description}}', settings.get('desc'));
        self.view.run_command("insert_snippet",
            {
                "contents": contents
            }
        )
