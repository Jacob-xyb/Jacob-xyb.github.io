import pandas as pd
import os


def reload_NintendoSwitchGame():
    path = os.path.dirname(__file__)
    df = pd.read_excel(os.path.join(path, 'NintendoSwitchGame.xlsx'), sheet_name=0)
    with open(os.path.join(path, 'index.html'), 'r', encoding='utf-8') as f:
        context = f.read()
    start_idx = context.find('<table>')
    end_idx = context.find('</table>') + len('</table>')
    inset_context = ""
    inset_context += '<table><tbody>\n'
    # 标题
    inset_context += '<tr>'
    for t_idx in range(df.shape[1] - 1):
        inset_context += f'<th>{df.columns[t_idx]}</th>'
    inset_context += '</tr>\n'
    for row in range(df.shape[0]):
        inset_context += '<tr>'
        for col in range(df.shape[1] - 1):
            if col == 0:
                inset_context += f'<td><a href="{df.iloc[row, -1]}" target="_blank">{df.iloc[row, col]}</a></td>'
            else:
                inset_context += f'<td>{df.iloc[row, col]}</td>'
        inset_context += '</tr>\n'
    inset_context += '</tbody></table>'
    new_context = context[:start_idx] + inset_context + context[end_idx:]
    with open(os.path.join(path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(new_context)


reload_NintendoSwitchGame()

if __name__ == '__main__':
    print(os.path.dirname(__file__))
