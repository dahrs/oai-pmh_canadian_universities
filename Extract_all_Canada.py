import os.path
import argparse
import jsonlines
from tqdm import tqdm
from oaipmh.client import Client
from utils.oai_tools import get_registry
from utils.environment import url_2_path_default


def extract_metadatas_formats(url: str) -> list:
    print("Harvesting: " + url)
    registry = get_registry()
    client = Client(url, registry)
    array_return = []
    for metadatas in client.listMetadataFormats():
        array_return.append(metadatas[0])
    return array_return


def extract(url: str, output_file: str, metadata_format: str = "oai_dc") -> None:
    print("Harvesting: " + url + " -> " + output_file)
    with jsonlines.open(output_file, 'w') as f_out:
        registry=get_registry()
        client = Client(url, registry)

        for record in tqdm(client.listRecords(metadataPrefix=metadata_format)):
            if record[1] is not None:
                data = record[1].getMap()
                # fds
                f_out.write(data)


mapping = {'urn:mpeg:mpeg21:2002:02-DIDL-NS http://standards.iso.org/ittf/PubliclyAvailableStandards/MPEG-21_schema_files/did/didl.xsd': 'didl',
           'http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-1.xsd': 'mods',
           'http://www.w3.org/2005/Atom http://www.kbcafe.com/rss/atom.xsd.xml': 'ore',
           'http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd': 'oai_dc',
           }

reverse_mapping = {item: key for key, item in mapping.items()}


def main(out_path: str):
    a_list = ["https://mru.arcabc.ca/oai2",
              "https://era.library.ualberta.ca/oai",
              "https://prism.ucalgary.ca/oai/request",
              "https://ecuad.arcabc.ca/oai2",
              "https://kora.kpu.ca/oai2",
              "https://viurrspace.ca/oai/request",
              "https://tru.arcabc.ca/oai2/",
              "https://twu.arcabc.ca/oai2/request",
              "https://unbc.arcabc.ca/oai2/",
              "https://ufv.arcabc.ca/oai2/",
              "https://roam.macewan.ca/server/oai/request",
              "https://dspace.library.uvic.ca/oai/request",
              "https://islandscholar.ca/oai2",
              "https://capu.arcabc.ca/oai2",
              "https://circuit.bcit.ca/repository/oai2",
              "https://winnspace.uwinnipeg.ca/oai/request",
              "https://mspace.lib.umanitoba.ca/oai/request",
              "https://udmscholar.cairnrepo.org/en/oai2",
              "https://scholar.acadiau.ca/oai2",
              "https://cbufaces.cairnrepo.org/oai2",
              "https://ec.msvu.ca/server/oai/request",
              "https://tspace.library.utoronto.ca/oai/request",
              "https://nscad.cairnrepo.org/oai2",
              "https://library2.smu.ca/oai/request",
              "https://stfxscholar.cairnrepo.org/oai2",
              "https://dr.library.brocku.ca/oai/request",
              "https://constellation.uqac.ca/cgi/oai2",
              "https://archipel.uqam.ca/cgi/oai2",
              "https://espace.rmc.ca/oai/request",
              "https://knowledgecommons.lakeheadu.ca/oai/request",
              "https://macsphere.mcmaster.ca/oai/request",
              "https://openresearch.ocadu.ca/cgi/oai2",
              "https://depot-e.uqtr.ca/cgi/oai2",
              "https://qspace.library.queensu.ca/oai/request",
              "https://ruor.uottawa.ca/oai/request",
              "https://zone.biblio.laurentian.ca/oai/request",
              "https://atrium.lib.uoguelph.ca/oai/request",
              "https://ir.library.ontariotechu.ca/oai/request",
              "https://uwspace.uwaterloo.ca/oai/request",
              "https://yorkspace.library.yorku.ca/oai/request",
              "https://espace.etsmtl.ca/cgi/oai2",
              "https://espace.enap.ca/cgi/oai2",
              "https://publications.polymtl.ca/cgi/oai2",
              "https://reflexion.hec.ca/in/rest/oai",
              "https://espace.inrs.ca/cgi/oai2",
              "https://papyrus.bib.umontreal.ca/oai/request",
              "https://r-libre.teluq.ca/cgi/oai2",
              "https://corpus.ulaval.ca/oai/request",
              "https://savoirs.usherbrooke.ca/oai/request",
              "https://harvest.usask.ca/oai/request",
              "https://research.library.mun.ca/cgi/oai2",
              "https://dalspace.library.dal.ca/oai/request",
              "https://dt.athabascau.ca/oai/request",
              "https://spectrum.library.concordia.ca/cgi/oai2",
              "https://depositum.uqat.ca/cgi/oai2",
              "https://curve.carleton.ca/oai-pmh/all",
              "https://ourspace.uregina.ca/oai/request",
              ]

    all_mm = []
    for oai_url in a_list:
        output_path = url_2_path_default(out_path, oai_url)
        if not os.path.isfile(output_path):
            extract(oai_url, output_file=output_path)
        all_metadatas_formats = extract_metadatas_formats(oai_url)
        all_mm.extend(all_metadatas_formats)
    print('Successfully extracted')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='VAE for data augmentation')
    # General arguments on training
    parser.add_argument('--out_path', type=str, default='.',
                        help="Path to the directory where the Dataset will be saved.")

    args = parser.parse_args()
    args = args.__dict__

    main(args['out_path'])
