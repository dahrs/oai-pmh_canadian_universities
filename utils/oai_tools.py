from oaipmh.metadata import MetadataReader, MetadataRegistry

oai_dc_reader_full = MetadataReader(
    fields={
        'identifier':  ('textList', 'oai_dc:dc/dc:identifier/text()'),
        'title':       ('textList', 'oai_dc:dc/dc:title/text()'),
        'type':        ('textList', 'oai_dc:dc/dc:type/text()'),
        'creator':     ('textList', 'oai_dc:dc/dc:creator/text()'),
        'publisher':   ('textList', 'oai_dc:dc/dc:publisher/text()'),
        'contributor': ('textList', 'oai_dc:dc/dc:contributor/text()'),
        'date':        ('textList', 'oai_dc:dc/dc:date/text()'),
        'format':      ('textList', 'oai_dc:dc/dc:format/text()'),
        'source':      ('textList', 'oai_dc:dc/dc:source/text()'),
        'language':    ('textList', 'oai_dc:dc/dc:language/text()'),
        'relation':    ('textList', 'oai_dc:dc/dc:relation/text()'),
        'coverage':    ('textList', 'oai_dc:dc/dc:coverage/text()'),
        'rights':      ('textList', 'oai_dc:dc/dc:rights/text()'),
        'subject':     ('textList', 'oai_dc:dc/dc:subject/text()'),
        'abstract':    ('textList', 'oai_dc:dc/dc:description/text()')},
    namespaces={
        'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
        'dc' :    'http://purl.org/dc/elements/1.1/'}
)



oai_etdms_reader = MetadataReader(
    fields={
        'identifier':  ('textList', 'etdms:thesis/etdms:identifier/text()'),
        'title':       ('textList', 'etdms:thesis/etdms:title/text()'),
        'type':        ('textList', 'etdms:thesis/etdms:type/text()'),
        'creator':     ('textList', 'etdms:thesis/etdms:creator/text()'),
        'publisher':   ('textList', 'etdms:thesis/etdms:publisher/text()'),
        'contributor': ('textList', 'etdms:thesis/etdms:contributor/text()'),
        'date':        ('textList', 'etdms:thesis/etdms:date/text()'),
        'format':      ('textList', 'etdms:thesis/etdms:format/text()'),
        'source':      ('textList', 'etdms:thesis/etdms:source/text()'),   
        'language':    ('textList', 'etdms:thesis/etdms:language/text()'),
        'relation':    ('textList', 'etdms:thesis/etdms:relation/text()'),
        'coverage':    ('textList', 'etdms:thesis/etdms:coverage/text()'),
        'rights':      ('textList', 'etdms:thesis/etdms:rights/text()'),
        'subject':     ('textList', 'etdms:thesis/etdms:subject/text()'),
        'abstract':    ('textList', 'etdms:thesis/etdms:description/text()'),
        'degree_name':    ('textList', 'etdms:thesis/etdms:degree/etdms:name/text()'),
        'degree_level':    ('textList', 'etdms:thesis/etdms:degree/etdms:level/text()'),
        'degree_grantor':    ('textList', 'etdms:thesis/etdms:degree/etdms:grantor/text()'),
        },
    namespaces={
        'etdms': 'http://www.ndltd.org/standards/metadata/etdms/1-0/'}
)


etdms_reader = MetadataReader(
fields={
'identifier': ('textList', 'etdms:thesis/etdms:identifier/text()'),
'title': ('textList', 'etdms:thesis/etdms:title/text()'),
'type': ('textList', 'etdms:thesis/etdms:type/text()'),
'creator': ('textList', 'etdms:thesis/etdms:creator/text()'),
'publisher': ('textList', 'etdms:thesis/etdms:publisher/text()'),
'contributor': ('textList', 'etdms:thesis/etdms:contributor/text()'),
'date': ('textList', 'etdms:thesis/etdms:date/text()'),
'language': ('textList', 'etdms:thesis/etdms:language/text()'),
'relation': ('textList', 'etdms:thesis/etdms:relation/text()'),
'subject': ('textList', 'etdms:thesis/etdms:subject/text()'),
'description': ('textList', 'etdms:thesis/etdms:description/text()')
},
namespaces={'etdms': 'http://www.ndltd.org/standards/metadata/etdms/1.0/'}
)

didl_reader = MetadataReader(
fields={
    'identifier': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/dii:Identifier/text()'),
    'title': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/oai_dc:dc/dc:title/text()'),
    'type': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/oai_dc:dc/dc:type/text()'),
    'creator': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/oai_dc:dc/dc:creator/text()'),
    'publisher': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/oai_dc:dc/dc:publisher/text()'),
    'contributor': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/oai_dc:dc/dc:contributor/text()'),
    'date': ('textList', 'didl:DIDL/didl:DIDLInfo/dcterms:created/text()'),
    'language': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/oai_dc:dc/dc:language/text()'),
    'relation': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/oai_dc:dc/dc:relation/text()'),
    'subject': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/oai_dc:dc/dc:subject/text()'),
    'description': ('textList', 'didl:DIDL/didl:Item/didl:Descriptor/didl:Statement/oai_dc:dc/dc:description/text()')},
    namespaces={
    'didl': 'urn:mpeg:mpeg21:2002:02-DIDL-NS',
    'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
    'dc' :    'http://purl.org/dc/elements/1.1/',
    'dii': 'urn:mpeg:mpeg21:2002:01-DII-NS',
    'dcterms': 'http://purl.org/dc/terms/'}
)

ore_reader = MetadataReader(
    fields={
    'identifier': ('textList', 'atom:entry/atom:id/text()'),
    'published': ('textList', 'atom:entry/atom:published/text()'),
    'updated': ('textList', 'atom:entry/atom:updated/text()'),
    'title': ('textList', 'atom:entry/atom:title/text()'),
    'author': ('textList', 'atom:entry/atom:author/atom:name/text()'),
    'date': ('textList', 'atom:entry/atom:published/text()'),
    'updated': ('textList', 'atom:entry/atom:updated/text()'),
    'generator': ('textList', 'atom:entry/atom:source/atom:generator/text()'),
    'aggregates': ('textList', 'atom:entry/atom:link[@rel="http://www.openarchives.org/ore/terms/aggregates"]/@href'),
    'description': ('textList', 'oreatom:triples/rdf:Description/dcterms:description/text()')
    },
    namespaces={
    'atom': 'http://www.w3.org/2005/Atom',
    'oreatom': 'http://www.openarchives.org/ore/atom/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dcterms': 'http://purl.org/dc/terms/'
}
)

oai_dc_reader = MetadataReader(
    fields={
        'identifier':  ('textList', 'oai_dc:dc/dc:identifier/text()'),
        'title':       ('textList', 'oai_dc:dc/dc:title/text()'),
        'type':        ('textList', 'oai_dc:dc/dc:type/text()'),
        'subject':     ('textList', 'oai_dc:dc/dc:subject/text()'),
        'abstract':    ('textList', 'oai_dc:dc/dc:description/text()')},
    namespaces={
        'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
        'dc' :    'http://purl.org/dc/elements/1.1/'}
)

qdc_reader = MetadataReader(
    fields = {
        'identifier': ('textList', 'qdc:qualifieddc/dc:identifier/text()'),
        'title':      ('textList', 'qdc:qualifieddc/dc:title/text()'),
        'type':       ('textList', 'qdc:qualifieddc/dc:type/text()'),
        'subject':    ('textList', 'qdc:qualifieddc/dc:subject/text()'),
        'abstract':   ('textList', 'qdc:qualifieddc/dcterms:abstract/text()')},
    namespaces={
        'qdc':     'http://dspace.org/qualifieddc/',
        'dc' :     'http://purl.org/dc/elements/1.1/',
        'dcterms': 'http://purl.org/dc/terms/'}
)

xoai_reader = MetadataReader(
    fields = {
        'identifier': ('textList', 'xoai:metadata//xoai:element[@name="identifier"]//xoai:field/text()'),
        'title':      ('textList', 'xoai:metadata//xoai:element[@name="title"]/xoai:element/xoai:field/text()'),
        'type':       ('textList', 'xoai:metadata//xoai:element[@name="type"]/xoai:element/xoai:field/text()'),
        'subject':    ('textList', 'xoai:metadata//xoai:element[@name="subject"]/xoai:element/xoai:field/text()'),
        'abstract':   ('textList', 'xoai:metadata//xoai:element[@name="abstract"]/xoai:element/xoai:field/text()')},
    namespaces={
        'dc' :     'http://purl.org/dc/elements/1.1/',
        'dcterms': 'http://purl.org/dc/terms/',
        'xoai':    'http://www.lyncode.com/xoai'}
)

mets_reader = MetadataReader(
fields={
'identifier': ('textList', 'mets:mets/mets:dmdSec/mets:mdWrap/mets:xmlData/mods:mods/mods:identifier/text()'),
'title': ('textList', 'mets:mets/mets:dmdSec/mets:mdWrap/mets:xmlData/mods:mods/mods:titleInfo/mods:title/text()'),
'type': ('textList', 'mets:mets/mets:dmdSec/mets:mdWrap/mets:xmlData/mods:mods/mods:typeOfResource/text()'),
'creator': ('textList', 'mets:mets/mets:dmdSec/mets:mdWrap/mets:xmlData/mods:mods/mods:name[mods:role/mods:roleTerm="author"]/mods:namePart/text()'),
'supervisor': ('textList', 'mets:mets/mets:dmdSec/mets:mdWrap/mets:xmlData/mods:mods/mods:name[mods:role/mods:roleTerm="supervisor"]/mods:namePart/text()'),
'dateIssued': ('textList', 'mets:mets/mets:dmdSec/mets:mdWrap/mets:xmlData/mods:mods/mods:originInfo/mods:dateIssued/text()'),
'abstract': ('textList', 'mets:mets/mets:dmdSec/mets:mdWrap/mets:xmlData/mods:mods/mods:abstract/text()'),
'language': ('textList', 'mets:mets/mets:dmdSec/mets:mdWrap/mets:xmlData/mods:mods/mods:language/mods:languageTerm/text()'),
'subject': ('textList', 'mets:mets/mets:dmdSec/mets:mdWrap/mets:xmlData/mods:mods/mods:subject/mods:topic/text()'),
},
namespaces={
'mets': 'http://www.loc.gov/METS/',
'mods': 'http://www.loc.gov/mods/v3'
}
)

mods_reader = MetadataReader(
fields={
'identifier': ('textList', 'mods:mods/mods:identifier/text()'),
'title': ('textList', 'mods:mods/mods:titleInfo/mods:title/text()'),
'type': ('textList', 'mods:mods/mods:typeOfResource/text()'),
'creator': ('textList', 'mods:mods/mods:name/mods:namePart/text()'),
'publisher': ('textList', 'mods:mods/mods:originInfo/mods:publisher/text()'),
'contributor': ('textList', 'mods:mods/mods:name/mods:namePart/text()'),
'date': ('textList', 'mods:mods/mods:originInfo/mods:dateIssued/text()'),
'format': ('textList', 'mods:mods/mods:physicalDescription/mods:form/text()'),
'language': ('textList', 'mods:mods/mods:language/mods:languageTerm/text()'),
'subject': ('textList', 'mods:mods/mods:subject/mods:topic/text()'),
'abstract': ('textList', 'mods:mods/mods:abstract/text()')},
namespaces={
'mods': 'http://www.loc.gov/mods/v3'}
)

dim_reader = MetadataReader(
    fields={
        'identifier':    ('textList', 'dim:dim/dim:field[@element="identifier" and @qualifier="uri"]/text()'),
        'title':         ('textList', 'dim:dim/dim:field[@element="title"]/text()'),
        'type':          ('textList', 'dim:dim/dim:field[@element="type"]/text()'),
        'creator':       ('textList', 'dim:dim/dim:field[@element="contributor" and @qualifier="author"]/text()'),
        'publisher':     ('textList', 'dim:dim/dim:field[@element="publisher"]/text()'),
        'contributor':   ('textList', 'dim:dim/dim:field[@element="contributor"]/text()'),
        'date':          ('textList', 'dim:dim/dim:field[@element="date"]/text()'),
        'format':        ('textList', 'dim:dim/dim:field[@element="format"]/text()'),
        'source':        ('textList', 'dim:dim/dim:field[@element="source"]/text()'),
        'language':      ('textList', 'dim:dim/dim:field[@element="language"]/text()'),
        'relation':      ('textList', 'dim:dim/dim:field[@element="relation"]/text()'),
        'coverage':      ('textList', 'dim:dim/dim:field[@element="coverage"]/text()'),
        'rights':        ('textList', 'dim:dim/dim:field[@element="rights"]/text()'),
        'subject':       ('textList', 'dim:dim/dim:field[@element="subject"]/text()'),
        'abstract':      ('textList', 'dim:dim/dim:field[@element="description" and @qualifier="abstract"]/text()')},
    namespaces={
        'dim': 'http://www.dspace.org/xmlns/dspace/dim'}
)

uketd_dc_reader = MetadataReader(
    fields={
        'identifier':  ('textList', 'uketd_dc:uketddc/dc:identifier/text()'),
        'title':       ('textList', 'uketd_dc:uketddc/dc:title/text()'),
        'type':        ('textList', 'uketd_dc:uketddc/dc:type/text()'),
        'creator':     ('textList', 'uketd_dc:uketddc/dc:creator/text()'),
        'publisher':   ('textList', 'uketd_dc:uketddc/dc:publisher/text()'),
        'contributor': ('textList', 'uketd_dc:uketddc/dc:contributor/text()'),
        'date':        ('textList', 'uketd_dc:uketddc/dcterms:issued/text()'),
        'format':      ('textList', 'uketd_dc:uketddc/dc:format/text()'),
        'source':      ('textList', 'uketd_dc:uketddc/dc:source/text()'),
        'language':    ('textList', 'uketd_dc:uketddc/dc:language/text()'),
        'relation':    ('textList', 'uketd_dc:uketddc/dc:relation/text()'),
        'coverage':    ('textList', 'uketd_dc:uketddc/dc:coverage/text()'),
        'rights':      ('textList', 'uketd_dc:uketddc/dc:rights/text()'),
        'subject':     ('textList', 'uketd_dc:uketddc/dc:subject/text()'),
        'abstract':    ('textList', 'uketd_dc:uketddc/dcterms:abstract/text()'),
        'institution': ('textList', 'uketd_dc:uketddc/uketdterms:institution/text()')},
    namespaces={
        'uketd_dc': 'http://naca.central.cranfield.ac.uk/ethos-oai/2.0/',
        'dc' :    'http://purl.org/dc/elements/1.1/',
        'dcterms': 'http://purl.org/dc/terms/',
        'uketdterms': 'http://naca.central.cranfield.ac.uk/ethos-oai/terms/'}
)

rdf_reader = MetadataReader(
    fields={
        'identifier':  ('textList', 'rdf:RDF/ow:Publication/dc:identifier/text()'),
        'title':       ('textList', 'rdf:RDF/ow:Publication/dc:title/text()'),
        'type':        ('textList', 'rdf:RDF/ow:Publication/dc:type/text()'),
        'creator':     ('textList', 'rdf:RDF/ow:Publication/dc:creator/text()'),
        'contributor': ('textList', 'rdf:RDF/ow:Publication/dc:contributor/text()'),
        'date':        ('textList', 'rdf:RDF/ow:Publication/dc:date/text()'),
        'language':    ('textList', 'rdf:RDF/ow:Publication/dc:language/text()'),
        'relation':    ('textList', 'rdf:RDF/ow:Publication/dc:relation/text()'),
        'publisher':   ('textList', 'rdf:RDF/ow:Publication/dc:publisher/text()'),
        'description': ('textList', 'rdf:RDF/ow:Publication/dc:description/text()'),
        'subject':     ('textList', 'rdf:RDF/ow:Publication/dc:subject/text()'),
    },
    namespaces={
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'ow': 'http://www.ontoworld.org/ow/1.1#',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }
)

marc_reader = MetadataReader(
fields={
'identifier': ('textList', 'marc:record/marc:datafield[@tag="024"]/marc:subfield[@code="a"]/text()'),
'title': ('textList', 'marc:record/marc:datafield[@tag="245"]/marc:subfield[@code="a"]/text()'),
'author': ('textList', 'marc:record/marc:datafield[@tag="720"]/marc:subfield[@code="a"]/text()'),
'publisher': ('textList', 'marc:record/marc:datafield[@tag="260"]/marc:subfield[@code="c"]/text()'),
'subject': ('textList', 'marc:record/marc:datafield[@tag="653"]/marc:subfield[@code="a"]/text()'),
'description': ('textList', 'marc:record/marc:datafield[@tag="520"]/marc:subfield[@code="a"]/text()'),
},
namespaces={
'marc': 'http://www.loc.gov/MARC21/slim'
}
)

oai_qdc_reader = MetadataReader(
    fields={
        'title':       ('textList', 'oai_qdc:dc/dc:title/text()'),
        'date':        ('textList', 'oai_qdc:dc/dc:date/text()'),
        'type':        ('textList', 'oai_qdc:dc/dc:type/text()'),
        'format':      ('textList', 'oai_qdc:dc/dc:format/text()'),
        'identifier':  ('textList', 'oai_qdc:dc/dc:identifier/text()'),
        'rights':      ('textList', 'oai_qdc:dc/dc:rights/text()')
    },
    namespaces={
        'oai_qdc': 'http://www.openarchives.org/OAI/2.0/oai_qdc/',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }
)

def get_registry() -> MetadataRegistry:
    registry = MetadataRegistry()
    registry.registerReader('qdc', qdc_reader)
    registry.registerReader('oai_etdms', oai_etdms_reader) #For convention measure, oai_etdms= etdms 1-0
    registry.registerReader('etdms', etdms_reader)
    registry.registerReader('oai_dc', oai_dc_reader_full)
    registry.registerReader('oai_qdc', oai_qdc_reader)
    registry.registerReader('mods', mods_reader)
    registry.registerReader('xoai', xoai_reader)
    registry.registerReader('didl', didl_reader)
    registry.registerReader('ore', ore_reader)
    registry.registerReader('mets', mets_reader)
    registry.registerReader('dim', dim_reader)
    registry.registerReader('uketd_dc', uketd_dc_reader)
    registry.registerReader('rdf', rdf_reader)
    registry.registerReader('marc', marc_reader)
    return registry
