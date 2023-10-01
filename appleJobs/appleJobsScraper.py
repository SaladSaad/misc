import requests
import re
from bs4 import BeautifulSoup as bs4

# parses home page to find max amount of pages


def findPages():
    url = "https://jobs.apple.com/en-us/search?location=united-states-USA&team=acoustic-technologies-HRDWR-ACT%20analog-and-digital-design-HRDWR-ADD%20architecture-HRDWR-ARCH%20battery-engineering-HRDWR-BE%20camera-technologies-HRDWR-CAM%20display-technologies-HRDWR-DISP%20engineering-project-management-HRDWR-EPM%20environmental-technologies-HRDWR-ENVT%20health-technology-HRDWR-HT%20machine-learning-and-ai-HRDWR-MCHLN%20mechanical-engineering-HRDWR-ME%20process-engineering-HRDWR-PE%20reliability-engineering-HRDWR-REL%20sensor-technologies-HRDWR-SENT%20silicon-technologies-HRDWR-SILT%20system-design-and-test-engineering-HRDWR-SDE%20wireless-hardware-HRDWR-WT%20quality-engineering-OPMFG-QE%20apps-and-frameworks-SFTWR-AF%20cloud-and-infrastructure-SFTWR-CLD%20core-operating-systems-SFTWR-COS%20devops-and-site-reliability-SFTWR-DSR%20engineering-project-management-SFTWR-EPM%20information-systems-and-technology-SFTWR-ISTECH%20machine-learning-and-ai-SFTWR-MCHLN%20security-and-privacy-SFTWR-SEC%20software-quality-automation-and-tools-SFTWR-SQAT%20wireless-software-SFTWR-WSFT%20machine-learning-infrastructure-MLAI-MLI%20deep-learning-and-reinforcement-learning-MLAI-DLRL%20natural-language-processing-and-speech-technologies-MLAI-NLP%20computer-vision-MLAI-CV%20applied-research-MLAI-AR&sort=locationAsc"

    path = './home.html'
    response = requests.get(url, stream=True)
    with open(path, 'w') as file:
        file.write(response.text)
    soup = bs4(open(path), 'html.parser')

    pagesElement = soup.find_all("span", class_="pageNumber")
    return (int(pagesElement[1].get_text())+1)

# iterates through each page and downloads file. You can parse each page as you iterate, but I'm saving them so that I can test different queries without having to access each page every time.


def mainDownloader(maxPages):
    path = './allPages.html'

    f = open(path, 'w')
    f.close()

    for page in range(1, maxPages):

        url = f"""https://jobs.apple.com/en-us/search?sort=locationAsc&location=united-states-USA&team=acoustic-technologies-HRDWR-ACT+analog-and-digital-design-HRDWR-ADD+architecture-HRDWR-ARCH+battery-engineering-HRDWR-BE+camera-technologies-HRDWR-CAM+display-technologies-HRDWR-DISP+engineering-project-management-HRDWR-EPM+environmental-technologies-HRDWR-ENVT+health-technology-HRDWR-HT+machine-learning-and-ai-HRDWR-MCHLN+mechanical-engineering-HRDWR-ME+process-engineering-HRDWR-PE+reliability-engineering-HRDWR-REL+sensor-technologies-HRDWR-SENT+silicon-technologies-HRDWR-SILT+system-design-and-test-engineering-HRDWR-SDE+wireless-hardware-HRDWR-WT+quality-engineering-OPMFG-QE+apps-and-frameworks-SFTWR-AF+cloud-and-infrastructure-SFTWR-CLD+core-operating-systems-SFTWR-COS+devops-and-site-reliability-SFTWR-DSR+engineering-project-management-SFTWR-EPM+information-systems-and-technology-SFTWR-ISTECH+machine-learning-and-ai-SFTWR-MCHLN+security-and-privacy-SFTWR-SEC+software-quality-automation-and-tools-SFTWR-SQAT+wireless-software-SFTWR-WSFT+machine-learning-infrastructure-MLAI-MLI+deep-learning-and-reinforcement-learning-MLAI-DLRL+natural-language-processing-and-speech-technologies-MLAI-NLP+computer-vision-MLAI-CV+applied-research-MLAI-AR&sort=locationAsc&page={page}"""

        response = requests.get(url, stream=True)
        with open(path, 'a') as file:
            file.write(response.text)


# finds all job ids in master file(allPages.html) and saves them to a .txt file without duplicates
def findJobIDs():
    path = './allPages.html'
    pattern = "/+\d+/"

    soup = bs4(open(path), 'html.parser')
    listings = soup.find_all("td", class_="table-col-1")

    allIDset = set()
    for listing in listings:
        id = re.search(pattern, str(listing)).group()[1:-1]
        allIDset.add(id)

    f = open('./allIDs.txt', 'w')
    f.close()

    f = open('./allIDs.txt', 'a')
    for id in allIDset:
        f.write(id)
        f.write('\n')
    f.close()


def main():
    # mainDownloader(findPages())
    findJobIDs()


if __name__ == '__main__':
    main()
