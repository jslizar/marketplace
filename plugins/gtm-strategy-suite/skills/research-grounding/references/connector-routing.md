# Connector Routing — which source answers which fact

Route each kind of fact to the best available source. Prefer the client's own
data and live tools over web search; prefer web search over the model's memory;
never source a number from memory alone. Tool names below are common examples —
use whatever the user has connected in each category.

| Fact you need | Best source category | Common tools |
|---|---|---|
| Company firmographics (employee count, revenue, industry, location) | Enrichment / sales-intel | Apollo, ZoomInfo, Clay |
| Lists of target accounts / contacts (bottom-up sizing) | Enrichment / sales-intel | Apollo, ZoomInfo, Clay |
| Technographics (what stack a company runs) | Enrichment / intent | ZoomInfo, Clay, BuiltWith-type |
| Web traffic, audience, competitive share-of-traffic | Web/competitive intel | SimilarWeb |
| Keyword volume, SEO/content gaps, backlinks | SEO intel | Ahrefs, SimilarWeb |
| Market size, growth rates, analyst figures | Web search → primary reports | Gartner/IDC/Statista, gov stats, trade bodies |
| Competitor positioning, pricing, launches, funding | Web search → company sources | Competitor sites, press, filings, Crunchbase-type |
| The client's own funnel, win rates, ACV, cycle, CAC | The client's CRM / analytics | HubSpot, Salesforce, the client's BI |
| The client's product usage / activation (for PLG) | Product analytics | Amplitude, the client's analytics |
| Sales/channel benchmark ranges (when client data is thin) | The gtm-benchmarks skill | bundled reference |

## Rules of thumb

- **Bottom-up sizing beats top-down.** Use an enrichment tool to count real
  target accounts, multiply by a defensible ACV. Cross-check against a top-down
  analyst figure.
- **The client's own CRM is the highest-value source** for anything about *their*
  funnel — never substitute an industry benchmark when the real number exists.
- **Benchmarks are a fallback, not a finding.** Use gtm-benchmarks only where the
  client's actual data isn't available, and label it as a benchmark range.
- **Always capture source + date.** A figure without provenance is an assumption.
