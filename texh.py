import os
import click

@click.command()
@click.option('-l', '--link', default='/home/zhiyuan/Note/all', prompt='pdf链接所在目录', help='在指定目录创建pdf链接')
@click.option('--code', is_flag=True, help='笔记中是否包含代码')
@click.option('-n', '--name', prompt='笔记名称', help='笔记名称')
def texh(link, code, name):
    cur_dir = os.getcwd()
    if os.path.exists(name):
        print('目录已存在')
        return
    os.makedirs(name + '/src')
    os.chdir(name + '/src')
    os.mknod(name + '.tex')
    pdf = name + '.pdf'
    os.system('ln -s ../output/%s %s/%s' % (pdf, link, pdf))

    if code:
        os.chdir('..')
        with open('.latexmkrc', 'w') as f:
            f.write('$xelatex="xelatex --shell-escape %O %S"')


if __name__ == '__main__':
    texh()
