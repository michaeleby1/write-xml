import pandas as pd


#############################
#  HELPER FUNCTIONS         #
#############################


def to_xml(row):
    """
    Converts row of Pandas DataFrame to XML format
    """
    xml = ['<item>']
    for col in row.index:
        xml.append(f'  <field name="{col}">{row[col]}</field>')
    xml.append('</item>')
    return '\n'.join(xml)


def df_to_xml(df):
    """
    Converts entire Pandas DataFrame to XML format
    """
    return '\n'.join(df.apply(to_xml, axis=1))


def write_xml(doc, filename, mode='w'):
    """
    Writes XML file
    """
    with open(filename, mode) as f:
        f.write('<root>\n')
        f.write(doc)
        f.write('\n</root>')


def main(df, filename, mode='w'):
    """
    Combines all functions in utils.py into one function
    """
    doc = df_to_xml(df)
    write_xml(doc, filename, mode)