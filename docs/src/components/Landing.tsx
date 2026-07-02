'use client'

import type { ReactNode } from 'react'
import { useEffect, useState } from 'react'
import { Link, useConfig } from 'vocs'
import IconArrowUpRight from '~icons/lucide/arrow-up-right'
import IconCheck from '~icons/lucide/check'
import IconCopy from '~icons/lucide/copy'
import IconGithub from '~icons/simple-icons/github'
import IconPython from '~icons/vscode-icons/file-type-python'
import IconUv from '~icons/vscode-icons/file-type-uv'

type InstallManager = 'pip' | 'uv'
type ThemeValue<value> = { dark: value; light: value }

const installManagers = ['uv', 'pip'] as const

const installIcons = {
  pip: <IconPython aria-hidden />,
  uv: <IconUv aria-hidden />,
} satisfies Record<InstallManager, ReactNode>

function getInstallCommand(manager: InstallManager, name: string) {
  if (manager === 'pip') return `pip install ${name}`
  return `uv add ${name}`
}

export function Landing(props: Landing.Props) {
  const config = useConfig()
  const [installManager, setInstallManager] = useState<InstallManager>('uv')
  const [copiedCommand, setCopiedCommand] = useState(false)
  const [copiedPrompt, setCopiedPrompt] = useState(false)
  const [docsUrl, setDocsUrl] = useState(props.docsOrigin ?? 'https://sentdoc.vercel.app')

  useEffect(() => {
    setDocsUrl(window.location.origin || props.docsOrigin || 'https://sentdoc.vercel.app')

    const { documentElement, body } = document
    const previousHtmlOverflow = documentElement.style.overflow
    const previousBodyOverflow = body.style.overflow

    documentElement.style.overflow = 'hidden'
    body.style.overflow = 'hidden'

    return () => {
      documentElement.style.overflow = previousHtmlOverflow
      body.style.overflow = previousBodyOverflow
    }
  }, [props.docsOrigin])

  const github = config.socials?.find((social) => social.icon === 'github')
  const logoUrl = props.logoUrl ?? config.logoUrl
  const title = props.title ?? config.title
  const description = props.description ?? config.description
  const agentPrompt = props.agentPrompt.replaceAll('{url}', docsUrl)

  async function copyCommand() {
    await navigator.clipboard.writeText(getInstallCommand(installManager, props.packageName))
    setCopiedCommand(true)
    setTimeout(() => setCopiedCommand(false), 2_000)
  }

  async function copyPrompt() {
    await navigator.clipboard.writeText(agentPrompt)
    setCopiedPrompt(true)
    setTimeout(() => setCopiedPrompt(false), 2_000)
  }

  const command = getInstallCommand(installManager, props.packageName)
  const [runner, ...args] = command.split(' ')

  return (
    <div className="vocs:relative vocs:left-1/2 vocs:z-50 vocs:mt-[calc(-1*var(--vocs-spacing-banner)-var(--vocs-spacing-content-py))] vocs:mb-[calc(-1*var(--vocs-spacing-content-py))] vocs:flex vocs:h-[100svh] vocs:w-screen vocs:-translate-x-1/2 vocs:flex-col vocs:overflow-hidden vocs:bg-primary vocs:text-heading vocs:max-[700px]:h-auto vocs:max-[700px]:min-h-[100svh] vocs:max-[700px]:overflow-visible">
      <div className="vocs:pointer-events-none vocs:absolute vocs:inset-0 vocs:opacity-35 vocs:dark:opacity-20 vocs:[background-image:repeating-linear-gradient(45deg,transparent_0_27px,light-dark(var(--vocs-color-gray12),var(--vocs-border-color-primary))_27px_28px,transparent_28px_56px),repeating-linear-gradient(-45deg,transparent_0_27px,light-dark(var(--vocs-color-gray12),var(--vocs-border-color-primary))_27px_28px,transparent_28px_56px)]" />

      <header className="vocs:relative vocs:pb-4 vocs:pt-8 vocs:max-[700px]:pt-6">
        <div className="vocs:mx-auto vocs:flex vocs:w-full vocs:max-w-[900px] vocs:items-center vocs:justify-between vocs:gap-6 vocs:px-8 vocs:max-[700px]:px-5">
          <div className="vocs:inline-flex vocs:items-center vocs:gap-[18px]">
            <Link to="/" aria-label={config.title} className="vocs:inline-flex vocs:no-underline">
              {logoUrl && typeof logoUrl === 'string' && (
                <img src={logoUrl} alt={config.title} className="vocs:h-6 vocs:w-auto" />
              )}
              {logoUrl && typeof logoUrl !== 'string' && (
                <>
                  <img
                    src={logoUrl.light}
                    alt={config.title}
                    className="vocs:h-6 vocs:w-auto vocs:dark:hidden"
                  />
                  <img
                    src={logoUrl.dark}
                    alt={config.title}
                    className="vocs:hidden vocs:h-6 vocs:w-auto vocs:dark:block"
                  />
                </>
              )}
              {!logoUrl && (
                <span className="vocs:text-[18px] vocs:font-semibold vocs:text-heading">
                  {config.title}
                </span>
              )}
            </Link>
            {props.logoSuffix}
          </div>
          <Link
            to={props.docsHref}
            className="vocs:inline-flex vocs:items-center vocs:gap-1.5 vocs:text-[13px] vocs:font-medium vocs:text-secondary vocs:no-underline vocs:transition-colors vocs:duration-100 vocs:hover:text-heading vocs:[&_svg]:size-3.5"
          >
            Docs
            <IconArrowUpRight aria-hidden />
          </Link>
        </div>
      </header>

      <main className="vocs:relative vocs:flex vocs:min-h-0 vocs:flex-1 vocs:items-center vocs:pb-10 vocs:pt-6 vocs:max-[700px]:items-start vocs:max-[700px]:pb-8 vocs:max-[700px]:pt-10">
        <div className="vocs:mx-auto vocs:w-full vocs:max-w-[900px] vocs:px-8 vocs:max-[700px]:px-5">
          <section className="vocs:w-[min(100%,700px)]">
            <h1 className="vocs:m-0 vocs:mb-[18px] vocs:text-[clamp(40px,5.6vw,68px)] vocs:font-semibold vocs:leading-[0.96] vocs:tracking-[-0.025em] vocs:text-heading vocs:max-[700px]:text-[clamp(40px,12vw,54px)]">
              {title}
            </h1>
            <p className="vocs:m-0 vocs:mb-8 vocs:text-xl vocs:leading-[1.6] vocs:text-secondary vocs:max-[700px]:text-[17px]">
              {description}
            </p>

            <div className="vocs:mb-10 vocs:flex vocs:flex-wrap vocs:gap-3">
              <Link
                to={props.docsHref}
                className="vocs:inline-flex vocs:min-h-12 vocs:items-center vocs:justify-center vocs:gap-2.5 vocs:rounded-[var(--vocs-radius-lg)] vocs:border vocs:border-solid vocs:border-accent vocs:bg-accent vocs:px-[22px] vocs:text-[15px] vocs:font-medium vocs:text-accentInvert vocs:no-underline vocs:transition-opacity vocs:duration-100 vocs:hover:opacity-90 vocs:max-[700px]:w-full vocs:[&_svg]:size-3.5"
              >
                Read the docs
                <IconArrowUpRight aria-hidden />
              </Link>
              {github && (
                <a
                  href={github.link}
                  target="_blank"
                  rel="noreferrer"
                  className="vocs:inline-flex vocs:min-h-12 vocs:items-center vocs:justify-center vocs:gap-2.5 vocs:rounded-[var(--vocs-radius-lg)] vocs:border vocs:border-solid vocs:border-primary vocs:bg-surface vocs:px-[22px] vocs:text-[15px] vocs:font-medium vocs:text-heading vocs:no-underline vocs:transition-colors vocs:duration-100 vocs:hover:border-secondary vocs:hover:bg-surfaceTint vocs:max-[700px]:w-full vocs:[&_svg]:size-3.5"
                >
                  <IconGithub aria-hidden />
                  GitHub
                </a>
              )}
            </div>

            <div className="vocs:mb-4 vocs:w-[min(100%,620px)] vocs:overflow-hidden vocs:rounded-[var(--vocs-radius-lg)] vocs:border vocs:border-solid vocs:border-primary vocs:bg-surface vocs:max-[700px]:w-full">
              <div className="vocs:flex vocs:items-stretch vocs:gap-1 vocs:border-b vocs:border-solid vocs:border-primary vocs:px-1">
                {installManagers.map((manager) => (
                  <button
                    key={manager}
                    type="button"
                    data-active={installManager === manager || undefined}
                    onClick={() => setInstallManager(manager)}
                    className={`vocs:-mb-px vocs:inline-flex vocs:cursor-pointer vocs:items-center vocs:gap-2 vocs:border-0 vocs:border-b-2 vocs:border-solid vocs:bg-transparent vocs:px-3.5 vocs:pb-[9px] vocs:pt-[11px] vocs:text-[13px] vocs:font-medium vocs:transition-colors vocs:duration-100 vocs:[&_svg]:size-[15px] ${
                      installManager === manager
                        ? 'vocs:border-white vocs:text-heading'
                        : 'vocs:border-transparent vocs:text-muted vocs:hover:text-heading'
                    }`}
                  >
                    {installIcons[manager]}
                    {manager}
                  </button>
                ))}
              </div>

              <button
                type="button"
                aria-label="Copy command"
                onClick={copyCommand}
                className="vocs:flex vocs:min-h-[68px] vocs:w-full vocs:cursor-pointer vocs:items-center vocs:gap-[18px] vocs:border-0 vocs:bg-transparent vocs:py-[18px] vocs:pl-0 vocs:pr-3 vocs:text-left vocs:transition-colors vocs:duration-100 vocs:hover:bg-surfaceTint"
              >
                <code className="vocs:font-mono vocs:text-lg vocs:text-accent">
                  <span className="vocs:text-muted">{runner}</span> {args.join(' ')}
                </code>
                <span
                  data-copied={copiedCommand || undefined}
                  className="vocs:ml-auto vocs:inline-flex vocs:size-8 vocs:items-center vocs:justify-center vocs:text-muted vocs:transition-colors vocs:duration-100 vocs:data-copied:text-success vocs:[&_svg]:size-4"
                >
                  {copiedCommand ? <IconCheck aria-hidden /> : <IconCopy aria-hidden />}
                </span>
              </button>
            </div>

            <button
              type="button"
              className="vocs:flex vocs:min-h-[52px] vocs:w-[min(100%,620px)] vocs:cursor-pointer vocs:items-center vocs:gap-3 vocs:rounded-[var(--vocs-radius-lg)] vocs:border vocs:border-solid vocs:border-primary vocs:bg-surface vocs:px-5 vocs:text-left vocs:text-[15px] vocs:font-normal vocs:text-secondary vocs:transition-colors vocs:duration-100 vocs:hover:bg-surfaceTint vocs:hover:text-heading vocs:max-[700px]:w-full"
              onClick={copyPrompt}
            >
              <span
                data-copied={copiedPrompt || undefined}
                className="vocs:inline-block vocs:size-[7px] vocs:bg-accent vocs:shadow-[0_0_10px_oklch(from_var(--vocs-color-accent)_l_c_h_/_28%)] vocs:data-copied:bg-success"
              />
              {copiedPrompt ? 'Copied to clipboard' : 'Copy setup instructions for agent'}
            </button>
          </section>
        </div>
      </main>
    </div>
  )
}

export declare namespace Landing {
  export type Props = {
    /** Prompt copied by the agent setup button. Use `{url}` for the docs origin. */
    agentPrompt: string
    /** Landing page description. Falls back to the site description. */
    description?: ReactNode | undefined
    /** Docs link URL. */
    docsHref: string
    /** Fallback docs origin when `window` is unavailable. */
    docsOrigin?: string | undefined
    /** Logo URL. Falls back to the site logo URL. */
    logoUrl?: string | ThemeValue<string> | undefined
    /** Content rendered next to the logo. */
    logoSuffix?: ReactNode | undefined
    /** Package name used for install commands. */
    packageName: string
    /** Landing page title. Falls back to the site title. */
    title?: ReactNode | undefined
  }
}
